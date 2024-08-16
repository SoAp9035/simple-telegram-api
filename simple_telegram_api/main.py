import requests

class TelegramBot:
    def __init__(self, token) -> None:
        """
        Args:
            token (str): Telegram bot token.
        """
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{self.token}"

    def send_message(self, chat_id, text, reply_to_message=False, message_id=None) -> dict:
        """
        Args:
            chat_id (int): The ID of the chat where you want to send the message.
            text (str): The message you want to send.
            reply_to_message (bool): True if you want to reply to a message. Default is False.
            message_id (int): The ID of the message you want to reply to. It is needed if reply_to_message is True.
        """
        url = f"{self.api_url}/sendMessage"
        if reply_to_message and message_id != None:
            data = {
            "chat_id": chat_id,
            "text": text,
            "reply_to_message_id": message_id
            }
        else:
            data = {
            "chat_id": chat_id,
            "text": text
            }
        response = requests.post(url, json=data)
        print(response.json())
        return response.json()
    
    def edit_message(self, chat_id, text, message_id) -> dict:
        """
        Args:
            chat_id (int): The ID of the chat where you want to send the message.
            text (str): New message.
            message_id (int): The ID of the message you want to edit.
        """
        url = f"{self.api_url}/editMessageText"
        data = {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": text
        }
        response = requests.post(url, json=data)
        return response.json()

    def get_updates(self, offset=None, timeout=30):
        """
        Get new messages.

        This method gets updates from the server.

        Args:
            offset (int): The ID of the last Update. Default is None.
            timeout (int): How long to wait for the updates. Default is 30 seconds.
        """
        url = f"{self.api_url}/getUpdates"
        data = {
            "timeout": timeout,
            "offset": offset
        }
        response = requests.post(url, json=data)

        if "result" in response.json():
            if response.json()["result"]:
                return response.json()
            else:
                return None
        else:
            print(f"Error {response.json()["error_code"]}: {response.json()["description"]}")
            return None
    
    def reset_updates(self, updates=None, timeout=5) -> None:
        """
        Clear old messages and get new ones.

        This method gets updates from the server and skips old messages.

        Args:
            updates (dict or None): Updates from `get_updates()`. If None, get new updates.
            timeout (int): How long to wait for the updates. Default is 5 seconds.

        Notes:
            If `updates` is not provided, new updates will be fetched automatically.
            Use the result from `get_updates()` as `updates`. (Recommended)
        """
        if updates is None:
            updates = self.get_updates(timeout=timeout)
        if updates:
            offset = updates["result"][-1]["update_id"] + 1
            self.get_updates(offset=offset, timeout=0)

