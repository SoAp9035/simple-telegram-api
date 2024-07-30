from simple_telegram_api import TelegramBot
import time

BOT_TOKEN = "BOT_TOKEN"

# Initialize the bot object with Telegram bot token
bot = TelegramBot(BOT_TOKEN)

# Infinite loop
while True:
    # Fetch last message from Telegram
    last_message = bot.get_last_message()

    chat_id = last_message["chat_id"]
    username = last_message["username"]
    last_text = last_message["text"]

    if last_message:
        # Send message to chat_id
        print(bot.send_message(chat_id=chat_id, text=f"You are @{username} and you just said {last_text}"))
        
        # Reset updates
        bot.reset_updates()
    
    time.sleep(1)
