from simple_telegram_api import TelegramBot

BOT_TOKEN = "BOT_TOKEN"

bot = TelegramBot(BOT_TOKEN)

# Skip old messages before bot is running.
bot.reset_updates()

print("Bot is running.")
while True:
    updates = bot.get_updates()

    # Check if it's empty.
    if updates:
        print(updates)
        bot.reset_updates(updates=updates)

        # For multiple coming up messages.
        for update in updates["result"]:
            chat_id = update["message"]["chat"]["id"]
            user_message = update["message"]["text"]
            
            bot_update = bot.send_message(user_message, chat_id=chat_id)
            print(bot_update)

