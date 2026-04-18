# File Change Notifier

A lightweight Obsidian plugin that shows a visual notification bubble whenever a file in your vault is modified.

## Features

- 🔔 Visual notification bubble appears when any file is modified
- ⚡ Lightweight and non-intrusive
- 🎨 Smooth fade-in/fade-out animations
- 🚀 Detects unsaved changes in real-time

## Installation

### Manual Installation (Development)

1. Navigate to your vault's plugin directory:
   ```
   .obsidian/plugins/notification-plugin/
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Build the plugin:
   ```
   npm run dev
   ```
   (Or `npm run build` for production)

4. Enable the plugin in Obsidian:
   - Open Obsidian Settings → Community Plugins
   - Disable "Restricted mode" if needed
   - Look for "File Change Notifier" and enable it

## How It Works

When you edit any file in your vault, a small blue notification bubble appears in the bottom-right corner for 2 seconds, then fades away.

### What Triggers the Notification

The notification appears when:
- ✅ You modify content in any open file
- ✅ You make unsaved changes
- ✅ Files are modified externally

## Customization

To customize the notification appearance, edit `src/main.ts` and modify the `createNotificationBubble()` method:

### Change the color:
```typescript
background-color: #FF6B6B; // Red instead of indigo
```

### Change the position:
```typescript
bottom: 50px;  // Move higher
right: 50px;   // Move more to the left
```

### Change the timeout duration:
```typescript
}, 3000); // Show for 3 seconds instead of 2
```

## Development

- `npm run dev` - Watch mode with incremental builds
- `npm run build` - Production build

## License

MIT
