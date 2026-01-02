// Initialize Telegram Web App
const tg = window.Telegram.WebApp;

// Expand to full height
tg.expand();

// Get user data
const user = tg.initDataUnsafe.user;
document.getElementById('user-id').textContent = user?.id || 'Unknown';

// Main button (optional)
tg.MainButton.setText('Submit').show().onClick(() => {
    tg.sendData(JSON.stringify({
        action: 'submit',
        userId: user.id
    }));
});

// Send data to bot
function sendData() {
    const data = {
        user_id: user?.id,
        action: 'button_click',
        timestamp: Date.now()
    };
    
    tg.sendData(JSON.stringify(data));
    tg.showAlert('Data sent to bot!');
}

// Close Mini App
function closeApp() {
    tg.close();
}

// Handle theme changes
tg.onEvent('themeChanged', () => {
    document.body.style.backgroundColor = tg.themeParams.bg_color || '#ffffff';
});

// Back button handler
tg.BackButton.show();
tg.onEvent('backButtonClicked', () => {
    // Handle back navigation
});

// Ready to show
tg.ready();