from simple_telegram_api import TelegramBot
import time

BOT_TOKEN = "BOT_TOKEN"

# Initialize the bot object with Telegram bot token
bot = TelegramBot(BOT_TOKEN)

# Infinite loop
while True:
    # Fetch last message from Telegram
    updates = bot.get_updates()
    
    if updates:
        for update in updates["result"]:
            update_id = update["update_id"]
            chat_id = update["message"]["chat"]["id"]
            username = update["message"]["from"]["username"]
            text = update["message"]["text"]

        # Send message to chat_id
        print(bot.send_message(chat_id=chat_id, text=f"You are @{username} and you just said {text}"))
        
        # Reset updates
        bot.reset_updates()
    
    time.sleep(1)
