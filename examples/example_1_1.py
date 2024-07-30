from simple_telegram_api import TelegramBot
import time

BOT_TOKEN = "BOT_TOKEN"

# Initialize the bot object with Telegram bot token
bot = TelegramBot(BOT_TOKEN)

# Variable to store last update id
last_update_id = None

# Infinite loop
while True:
    # Fetch updates from Telegram
    updates = bot.get_updates(offset=last_update_id)

    if updates:
        for update in updates["result"]:
            update_id = update["update_id"]
            chat_id = update["message"]["chat"]["id"]
            username = update["message"]["from"]["username"]
            text = update["message"]["text"]

            # Update the last update id to next one
            last_update_id = update_id + 1

            # Send message to chat_id
            bot.send_message(chat_id, f"You are @{username} and you said: {text}")

    time.sleep(1)