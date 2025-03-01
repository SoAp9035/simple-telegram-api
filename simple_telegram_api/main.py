import requests


class TelegramBot:
    def __init__(self, token: str) -> None:
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{self.token}"

    def send_message(self, text: str, chat_id: int, reply_to_message: bool = False, message_id: int = None) -> dict | None:
        """
        Args:
            text (str): The message you want to send.
            chat_id (int): The ID of the chat where you want to send the message.
            reply_to_message (bool): True if you want to reply to a message. Default is False.
            message_id (int): The ID of the message you want to reply to. It is needed if reply_to_message is True.
        """
        url = f"{self.api_url}/sendMessage"
        if reply_to_message and message_id != None:
            data = {
            "text": text,
            "chat_id": chat_id,
            "reply_to_message_id": message_id
            }
        else:
            data = {
            "text": text,
            "chat_id": chat_id
            }
        response = requests.post(url, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            try:
               error_msg = f"Error {response.json()["error_code"]}: {response.json()["description"]}"
            except Exception:
                error_msg = f"Error {response.status_code}: {response.text}"
            finally:
                print(error_msg)
                return None
    
    def edit_message(self, text: str, chat_id: int, message_id: int) -> dict | None:
        """
        Args:
            text (str): New message.
            chat_id (int): The ID of the chat where you want to send the message.
            message_id (int): The ID of the message you want to edit.
        """
        url = f"{self.api_url}/editMessageText"
        data = {
            "text": text,
            "chat_id": chat_id,
            "message_id": message_id
        }
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            return response.json()
        else:
            try:
               error_msg = f"Error {response.json()["error_code"]}: {response.json()["description"]}"
            except Exception:
                error_msg = f"Error {response.status_code}: {response.text}"
            finally:
                print(error_msg)
                return None

    def get_updates(self, offset: int = None, timeout: int = 30) -> dict | None:
        """
        Get new messages.

        This method gets updates from Telegram.

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

        if response.status_code == 200:
            return response.json()
        else:
            try:
               error_msg = f"Error {response.json()["error_code"]}: {response.json()["description"]}"
            except Exception:
                error_msg = f"Error {response.status_code}: {response.text}"
            finally:
                print(error_msg)
                return None
    
    def reset_updates(self, updates=None, timeout=5) -> None:
        """
        Clear old messages and get new ones.

        This method gets updates from Telegram and skips old messages.

        Args:
            updates (dict or None): Updates from `get_updates()`. If None, get new updates.
            timeout (int): How long to wait for the updates. Default is 5 seconds.

        Notes:
            If `updates` is not provided, new updates will be fetched automatically.
            Use the result from `get_updates()` as `updates`. (Recommended)
        """
        if updates:
            offset = updates["result"][-1]["update_id"] + 1
            self.get_updates(offset=offset, timeout=0)
        else:
            updates = self.get_updates(timeout=timeout)
