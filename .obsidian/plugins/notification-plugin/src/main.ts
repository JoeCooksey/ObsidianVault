import { Plugin, App } from 'obsidian';

export default class FileChangeNotifierPlugin extends Plugin {
	private notificationElement: HTMLElement | null = null;
	private hideTimeout: NodeJS.Timeout | null = null;

	async onload() {
		console.log('File Change Notifier plugin loaded');

		// Create the notification bubble element
		this.createNotificationBubble();

		// Listen for file modifications
		this.registerEvent(
			this.app.vault.on('modify', (file) => {
				this.showNotification();
			})
		);
	}

	onunload() {
		console.log('File Change Notifier plugin unloaded');

		// Clean up notification element
		if (this.notificationElement) {
			this.notificationElement.remove();
			this.notificationElement = null;
		}

		// Clear any pending hide timeout
		if (this.hideTimeout) {
			clearTimeout(this.hideTimeout);
			this.hideTimeout = null;
		}
	}

	private createNotificationBubble() {
		// Create the bubble container
		const bubble = document.createElement('div');
		bubble.className = 'file-change-bubble';
		bubble.id = 'file-change-notifier-bubble';

		// Add inline styles for the notification bubble
		bubble.style.cssText = `
			position: fixed;
			bottom: 20px;
			right: 20px;
			width: 12px;
			height: 12px;
			border-radius: 50%;
			background-color: #4f46e5;
			box-shadow: 0 2px 8px rgba(79, 70, 229, 0.3);
			opacity: 0;
			pointer-events: none;
			z-index: 1000;
			transition: opacity 0.3s ease-in-out;
		`;

		document.body.appendChild(bubble);
		this.notificationElement = bubble;
	}

	private showNotification() {
		if (!this.notificationElement) return;

		// Clear any existing hide timeout
		if (this.hideTimeout) {
			clearTimeout(this.hideTimeout);
		}

		// Show the bubble with fade-in effect
		this.notificationElement.style.opacity = '1';

		// Auto-hide after 2 seconds
		this.hideTimeout = setTimeout(() => {
			if (this.notificationElement) {
				this.notificationElement.style.opacity = '0';
			}
			this.hideTimeout = null;
		}, 2000);
	}
}
