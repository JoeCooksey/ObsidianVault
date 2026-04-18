#!/usr/bin/env python3
"""
BM25 search tool for Joe_Vault markdown wiki.

Usage:
    python search.py "query terms" [--dir PATH] [--top-k N] [--rebuild] [--no-rebuild] [--cache-dir PATH]
"""

import argparse
import os
import pickle
import re
import sys
import time


MAX_FILE_SIZE = 500 * 1024  # 500 KB


def get_md_files(search_dir):
    """Walk search_dir and return sorted list of absolute .md file paths."""
    results = []
    cache_dir_name = ".search_cache"
    for root, dirs, files in os.walk(search_dir):
        # Skip .search_cache directory
        dirs[:] = [d for d in dirs if d != cache_dir_name]
        for fname in files:
            if not fname.endswith(".md"):
                continue
            if fname.endswith(".excalidraw.md"):
                continue
            fpath = os.path.join(root, fname)
            try:
                if os.path.getsize(fpath) > MAX_FILE_SIZE:
                    continue
            except OSError:
                continue
            results.append(fpath)
    return sorted(results)


def is_cache_fresh(cache_path, md_files, search_dir):
    """Return True if the pickle cache is newer than all .md files and search_dir."""
    if not os.path.exists(cache_path):
        return False
    try:
        with open(cache_path, "rb") as f:
            index = pickle.load(f)
        built_at = index.get("built_at", 0)
        # Check search_dir mtime (catches deletions)
        if os.path.getmtime(search_dir) > built_at:
            return False
        for fpath in md_files:
            if os.path.getmtime(fpath) > built_at:
                return False
        return True
    except Exception:
        return False


def extract_title(lines, filename):
    """Extract H1 heading or fall back to filename stem."""
    in_frontmatter = False
    frontmatter_done = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if i == 0 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
                frontmatter_done = True
            continue
        m = re.match(r"^#\s+(.+)", line)
        if m:
            return m.group(1).strip()
    # Fallback: filename stem
    stem = os.path.splitext(os.path.basename(filename))[0]
    return re.sub(r"[_\-]+", " ", stem)


def preprocess(lines):
    """Return a flat list of lowercase tokens for BM25 indexing."""
    # Strip YAML frontmatter
    text_lines = []
    in_frontmatter = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if i == 0 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            continue
        text_lines.append(line)

    text = "\n".join(text_lines)

    # Strip Excalidraw JSON blocks (content between %% delimiters)
    text = re.sub(r"%%.*?%%", " ", text, flags=re.DOTALL)

    # Expand Obsidian wikilinks [[display|alias]] -> alias, [[display]] -> display
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)

    # Strip URLs
    text = re.sub(r"https?://\S+", " ", text)

    # Strip markdown syntax characters
    text = re.sub(r"[#*_`\[\]()>!~]", " ", text)

    # Lowercase and tokenize
    tokens = re.findall(r"\b[a-z][a-z0-9]*\b", text.lower())
    return tokens


def build_index(search_dir, md_files):
    """Read all files, preprocess, fit BM25, return index dict."""
    from rank_bm25 import BM25Okapi

    doc_ids = []
    titles = []
    raw_lines_list = []
    corpus = []

    search_dir_norm = search_dir.replace("\\", "/")

    for fpath in md_files:
        try:
            with open(fpath, encoding="utf-8", errors="replace") as f:
                lines = f.readlines()
        except OSError:
            continue

        rel = os.path.relpath(fpath, search_dir).replace("\\", "/")
        title = extract_title(lines, fpath)
        tokens = preprocess(lines)

        doc_ids.append(rel)
        titles.append(title)
        raw_lines_list.append([l.rstrip("\n") for l in lines])
        corpus.append(tokens if tokens else [""])

    bm25 = BM25Okapi(corpus)

    return {
        "built_at": time.time(),
        "search_dir": search_dir_norm,
        "doc_ids": doc_ids,
        "titles": titles,
        "raw_lines": raw_lines_list,
        "bm25": bm25,
    }


def save_index(index, cache_path):
    """Pickle the index to cache_path, creating the directory if needed."""
    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    with open(cache_path, "wb") as f:
        pickle.dump(index, f)


def load_index(cache_path):
    """Load and return the pickled index."""
    with open(cache_path, "rb") as f:
        return pickle.load(f)


def extract_context(raw_lines, query_terms, max_snippets=2):
    """Return up to max_snippets lines that best match query_terms."""
    if not query_terms:
        return []

    scored = []
    for i, line in enumerate(raw_lines):
        lower = line.lower()
        score = sum(1 for t in query_terms if t in lower)
        if score > 0:
            scored.append((score, i, line))

    # Sort by score desc, take top max_snippets, then re-sort by original line order
    top = sorted(scored, key=lambda x: x[0], reverse=True)[:max_snippets]
    top.sort(key=lambda x: x[1])

    snippets = []
    for _, _, line in top:
        line = line.strip()
        if len(line) > 120:
            line = line[:120] + "..."
        snippets.append(line)
    return snippets


def tokenize_query(query):
    """Tokenize query the same way as preprocess."""
    return re.findall(r"\b[a-z][a-z0-9]*\b", query.lower())


def search(index, query, top_k):
    """Run BM25 query, return list of result dicts."""
    query_tokens = tokenize_query(query)
    if not query_tokens:
        return []

    scores = index["bm25"].get_scores(query_tokens)
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)

    results = []
    for doc_i, score in ranked:
        if score <= 0.0:
            break
        if len(results) >= top_k:
            break
        context = extract_context(index["raw_lines"][doc_i], query_tokens)
        results.append({
            "path": index["doc_ids"][doc_i],
            "title": index["titles"][doc_i],
            "score": score,
            "context": context,
        })

    return results


def format_results(results, query, top_k, total_above_threshold):
    """Render results as a consistent text block."""
    lines = []
    lines.append(f'SEARCH: "{query}"')
    lines.append(f"RESULTS: {len(results)} of {top_k} requested ({total_above_threshold} had score > 0)")
    lines.append("---")

    for i, r in enumerate(results, 1):
        lines.append(f"RESULT {i}")
        lines.append(f"PATH: {r['path']}")
        lines.append(f"TITLE: {r['title']}")
        lines.append(f"SCORE: {r['score']:.3f}")
        if r["context"]:
            lines.append("CONTEXT:")
            for c in r["context"]:
                lines.append(f"  > {c}")
        lines.append("---")

    lines.append("END SEARCH")
    return "\n".join(lines)


def main():
    # Force UTF-8 output on Windows to handle emoji and non-ASCII characters
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(
        description="BM25 search over markdown files in a vault/wiki directory."
    )
    parser.add_argument("query", nargs="?", default="", help="Search query string")
    parser.add_argument(
        "--dir",
        default=os.path.dirname(os.path.abspath(__file__)),
        help="Directory to index (default: directory containing search.py)",
    )
    parser.add_argument("--top-k", type=int, default=10, help="Number of results (default: 10)")
    parser.add_argument("--rebuild", action="store_true", help="Force full index rebuild")
    parser.add_argument("--no-rebuild", action="store_true", help="Use cache even if stale")
    parser.add_argument("--cache-dir", default=None, help="Override .search_cache directory location")
    args = parser.parse_args()

    query = args.query.strip()
    if not query:
        print("ERROR: No query provided.", file=sys.stderr)
        print("Usage: python search.py \"your query\" [--top-k N]", file=sys.stderr)
        sys.exit(1)

    search_dir = os.path.abspath(args.dir)
    if not os.path.isdir(search_dir):
        print(f"ERROR: Directory not found: {search_dir}", file=sys.stderr)
        sys.exit(1)

    cache_base = args.cache_dir if args.cache_dir else os.path.join(search_dir, ".search_cache")
    cache_path = os.path.join(cache_base, "bm25_index.pkl")

    md_files = get_md_files(search_dir)
    if not md_files:
        print(f"ERROR: No .md files found in {search_dir}", file=sys.stderr)
        sys.exit(1)

    # Determine whether to use cache or rebuild
    if args.rebuild:
        use_cache = False
    elif args.no_rebuild:
        use_cache = os.path.exists(cache_path)
    else:
        use_cache = is_cache_fresh(cache_path, md_files, search_dir)

    if use_cache:
        index = load_index(cache_path)
    else:
        print(f"Building index over {len(md_files)} files...", file=sys.stderr)
        index = build_index(search_dir, md_files)
        save_index(index, cache_path)
        print("Index built and cached.", file=sys.stderr)

    # Count total above threshold before limiting to top_k
    query_tokens = tokenize_query(query)
    all_scores = index["bm25"].get_scores(query_tokens) if query_tokens else []
    total_above = sum(1 for s in all_scores if s > 0.0)

    results = search(index, query, args.top_k)
    print(format_results(results, query, args.top_k, total_above))


if __name__ == "__main__":
    main()
