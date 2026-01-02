from flask import Flask, request, jsonify
import telebot
import os

app = Flask(__name__)
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
WEB_APP_URL = 'https://your-domain.com/index.html'  # Your Mini App URL

bot = telebot.TeleBot(TOKEN)

# Command to open Mini App
@bot.message_handler(commands=['start', 'app'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(
        text="Open Mini App 🚀",
        web_app=telebot.types.WebAppInfo(url=WEB_APP_URL)
    )
    markup.add(button)
    
    bot.send_message(
        message.chat.id,
        "Click the button below to open the Mini App:",
        reply_markup=markup
    )

# Handle data from Mini App
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = json.loads(message.web_app_data.data)
    user_id = data.get('user_id')
    action = data.get('action')
    
    # Process the data
    response = f"Received from Mini App:\nUser ID: {user_id}\nAction: {action}"
    bot.send_message(message.chat.id, response)

# Set bot commands
bot.set_my_commands([
    telebot.types.BotCommand("start", "Start the bot"),
    telebot.types.BotCommand("app", "Open Mini App")
])

# Flask endpoint for receiving data (alternative method)
@app.route('/web-data', methods=['POST'])
def web_data():
    data = request.json
    # Process data here
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    # Start bot polling in a separate thread
    import threading
    threading.Thread(target=bot.infinity_polling).start()
    
    # Start Flask server
    app.run(port=5000)
    