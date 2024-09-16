# Simple Telegram Api

A simple and easy-to-use Python library for Telegram bots. This library allows you to send messages, edit messages, fetch updates, and handle messages easily.

## Installation

Installation using pip (a Python package manager):

```
pip install simple-telegram-api
```

## Usage/Examples

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
            user_message = update["message"]["text"]
            
            bot_update = bot.send_message(user_message, chat_id=chat_id)
            print(bot_update)
```

### Using the TelegramBot Class

```python
from simple_telegram_api import TelegramBot

bot = TelegramBot('BOT_TOKEN')
```

### Get Updates

This function gets new messages from Telegram.

```python
updates = bot.get_updates()
```

### Reset Updates

This function gets updates from Telegram and skips old messages.

```python
bot.reset_updates()
```

### Send Message

To send a message:

```python
bot.send_message(text=text, chat_id=chat_id)
```

To reply to a message:

```python
bot.send_message(text=text, chat_id=chat_id, reply_to_message=True, message_id=message_id)
```

### Edit Message

```python
bot.edit_message(text=text, chat_id=chat_id, message_id=message_id)
```

## Recommendations

If `updates` is not provided in `reset_updates()`, new updates will be fetched automatically. Use the result from `get_updates()` as `updates`, as shown in the example.

## License

[MIT](https://choosealicense.com/licenses/mit/)
