# Simple Telegram API

A simple and easy-to-use Python wrapper for Telegram bots. This library allows you to send messages, edit messages, fetch updates, and handle messages easily.

## Getting a Bot Token

To get a bot token, message [@BotFather](https://t.me/botfather) on Telegram and follow the instructions to create a new bot. BotFather will provide you with a token that looks like `123456789:ABCdefGHIjklmNOPQrstUVwxyz`.

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

# Delete old messages before bot is running.
bot.reset_updates()

print("Bot is running.")
while True:
    updates = bot.get_updates()

    # Check if it's empty.
    if updates["result"]:
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

#### Example Get Updates Output

Here is an example of the output from the `get_updates()` function:

```python
{
    "ok": True,
    "result": [
        {
            "update_id": 123456789,
            "message": {
                "message_id": 123,
                "from": {
                    "id": 123456789,
                    "is_bot": False,
                    "first_name": "Person Name",
                    "username": "person",
                    "language_code": "en"
                },
                "chat": {
                    "id": 123456789,
                    "first_name": "Person Name",
                    "username": "person",
                    "type": "private"
                },
                "date": 1733920402,
                "text": "Hi!"
            }
        }
    ]
}
```

### Reset Updates

This function deletes old messages from updates.

```python
bot.reset_updates(updates=updates)
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

#### Example Send Message Output

Here is an example of the output from the `send_message()` function:

```python
{
    "ok": True,
    "result": {
        "message_id": 124,
        "from": {
            "id": 123456789,
            "is_bot": True,
            "first_name": "Bot",
            "username": "bot"
        },
        "chat": {
            "id": 123456789,
            "first_name": "Person Name",
            "username": "person",
            "type": "private"
        },
        "date": 1733920404,
        "text": "Hi!"
    }
}
```

### Edit Message

```python
bot.edit_message(text=text, chat_id=chat_id, message_id=message_id)
```

## Recommendations

If `updates` is not provided in `reset_updates()`, new updates will be fetched automatically. Use the result from `get_updates()` as `updates`, as shown in the example.

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.