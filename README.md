# Simple Telegram Bot

A simple and easy-to-use Python library for Telegram bots. This library allows you to send messages, edit messages, fetch updates, and handle messages easily.

## Installation

Installation using pip (a Python package manager):

```
pip install simple-telegram-api
```

## Example

A simple echo bot:

```python
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
            user_text = update["message"]["text"]
            
            bot_message = bot.send_message(chat_id=chat_id, text=user_text)
```

## Recommendations

If `updates` is not provided in `reset_updates()`, new updates will be fetched automatically. Use the result from `get_updates()` as `updates`, as shown in the example.

## License

[MIT](https://choosealicense.com/licenses/mit/)
