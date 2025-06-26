from simple_telegram_api import TelegramBot

bot = TelegramBot("BOT_TOKEN")

def echo_bot():
    updates = bot.get_updates()
    if updates["result"]:
        for update in updates["result"]:
            text, chat_id = (
                update["message"]["text"],
                update["message"]["chat"]["id"],
            )
            bot.send_message(text, chat_id)

        # Update offset to skip already processed messages in future calls.
        bot.reset_updates(updates=updates)

if __name__ == "__main__":
    bot.start_loop(echo_bot)
