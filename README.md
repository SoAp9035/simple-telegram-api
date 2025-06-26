# Simple Telegram API

A simple and easy-to-use Python wrapper for Telegram bots. This library allows you to send messages, edit messages, fetch updates, handle messages, and run continuous loops easily.

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
```

### Using the TelegramBot Class

```python
from simple_telegram_api import TelegramBot

bot = TelegramBot("BOT_TOKEN")
```

### Get Bot Information

Get information about your bot:

```python
bot_info = bot.get_me()
print(bot_info)
```

### Get Updates

This function gets new messages from Telegram with optional parameters:

```python
# Basic usage
updates = bot.get_updates()

# Advanced usage with parameters
updates = bot.get_updates(
    offset=None,          # Identifier of the first update to be returned
    limit=100,            # Limits the number of updates (1-100)
    timeout=0,            # Timeout in seconds for long polling
    allowed_updates=None  # List of update types to receive
)
```

#### Example Get Updates Output

Here is an example of the output from the `get_updates()` function:

```python
{
    'ok': True,
    'result': [
        {
            'update_id': 123456789,
            'message': {
                'message_id': 123,
                'from': {
                    'id': 123456789,
                    'is_bot': False,
                    'first_name': 'Person Name',
                    'username': 'username',
                    'language_code': 'en'
                },
                'chat': {
                    'id': 123456789,
                    'first_name': 'Person Name',
                    'username': 'username',
                    'type': 'private'
                },
                'date': 123456789,
                'text': 'Hello!'
            }
        }
    ]
}
```

### Reset Updates

This function deletes old messages from updates. If no updates are provided, it will automatically fetch new ones:

```python
# With updates parameter (Recommended)
bot.reset_updates(updates=updates)

# Without updates parameter (will fetch automatically)
bot.reset_updates()
```

### Send Message

To send a message:

```python
bot.send_message(text="Hello!", chat_id=chat_id)
```

To send a message with additional parameters:

```python
bot.send_message(
    text="Hello!",
    chat_id=chat_id,
    parse_mode="Markdown",
    reply_to_message_id=message_id
)
```

#### Example Send Message Output

Here is an example of the output from the `send_message()` function:

```python
{
    'ok': True,
    'result': {
        'message_id': 123,
        'from': {
            'id': 1234567890,
            'is_bot': True,
            'first_name': 'Bot',
            'username': 'my_bot'
        },
        'chat': {
            'id': 123456789,
            'first_name': 'Person Name',
            'username': 'username',
            'type': 'private'
        },
        'date': 123456789,
        'text': 'Hello!'
    }
}
```

### Edit Message

Edit an existing message:

```python
bot.edit_message(text="Updated text", chat_id=chat_id, message_id=message_id)
```

Edit with additional parameters:

```python
bot.edit_message(
    text="Updated text",
    chat_id=chat_id,
    message_id=message_id,
    parse_mode="Markdown"
)
```

#### Example Edit Message Output

Here is an example of the output from the `edit_message()` function:

```python
{
    'ok': True,
    'result': {
        'message_id': 123,
        'from': {
            'id': 1234567890,
            'is_bot': True,
            'first_name': 'Bot',
            'username': 'my_bot'
        },
        'chat': {
            'id': 123456789,
            'first_name': 'Person Name',
            'username': 'username',
            'type': 'private'
        },
        'date': 123456789,
        'edit_date': 123456790,
        'text': 'Updated text'
    }
}
```

### Start Loop

Run continuous callback functions at set intervals:

```python
def get_messages():
    # Function to retrieve messages (to be implemented)
    pass

def say_hello():
    # This function will be called repeatedly by the loop
    pass

# Start the loop, calling get_messages and say_hello every 1 second
bot.start_loop(get_messages, say_hello, interval=1.0)
```

## Error Handling

The library includes custom exception:
- `TelegramBotError`: TelegramBot Error.

## Requirements

- Python >= 3.10
- requests==2.32.4

## Recommendations

- If `updates` is not provided in `reset_updates()`, new updates will be fetched automatically
- Use the result from `get_updates()` as `updates` parameter in `reset_updates()` for better performance
- Use the `start_loop()` method for continuous bot operation with custom callback functions

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.

## Links

- [GitHub Repository](https://github.com/SoAp9035/simple-telegram-api)
- [PyPI Package](https://pypi.org/project/simple-telegram-api/)
- [Buy Me a Coffee](https://buymeacoffee.com/soap9035/)
- [Visit My Website](https://ahmetburhan.com/)