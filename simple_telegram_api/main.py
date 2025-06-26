import json
import requests
from .exceptions import TelegramBotError


class TelegramBot:
    """
    A simple and easy-to-use Python wrapper for Telegram bots.
    """
    def __init__(self, token: str = "YOUR_BOT_TOKEN") -> None:
        """
        Initialize the TelegramBot instance.

        Args:
            token (str): The bot token provided by BotFather.
        """
        self._token = token
        self._api_endpoint = f"https://api.telegram.org/bot{self._token}"

    def get_me(self) -> dict:
        """
        Fetch information about the bot.

        Returns:
            dict: Bot information as returned by the Telegram API.

        Raises:
            TelegramBotError: If the request fails.
        """
        try:
            response = requests.get(self._api_endpoint + "/getMe")
            response.raise_for_status()
        except Exception as e:
            raise TelegramBotError(e)

        return response.json()

    def get_updates(
        self,
        offset: int | None = None,
        limit: int = 100,
        timeout: int = 0,
        allowed_updates: list[str] | None = None,
    ) -> dict:
        """
        Fetch received messages and updates for the bot.

        Args:
            offset (int, optional): Identifier of the first update to be returned.
            limit (int, optional): Limits the number of updates to be retrieved.
            timeout (int, optional): Timeout in seconds for long polling.
            allowed_updates (list[str], optional): List of update types to receive.

        Returns:
            dict: Updates as returned by the Telegram API.

        Raises:
            TelegramBotError: If the request fails.
        """
        params = {"limit": limit, "timeout": timeout}

        # Optional parameters
        if offset is not None:
            params["offset"] = offset
        if allowed_updates:
            params["allowed_updates"] = json.dumps(allowed_updates)

        # Send request to telegram api for updates
        try:
            response = requests.get(self._api_endpoint + "/getUpdates", params=params)
            response.raise_for_status()
        except Exception as e:
            raise TelegramBotError(e)

        return response.json()

    def reset_updates(self, updates: dict | None = None) -> None:
        """
        Resets the update offset to skip already processed messages. If no updates are provided, it will automatically fetch new ones.

        Args:
            updates (dict, optional): The updates dictionary returned by the Telegram API.
        """
        if updates is None:
            updates = self.get_updates()
        try: 
            if updates.get("result"):
                last_offset = updates["result"][-1]["update_id"]
                self.get_updates(offset=last_offset + 1)
        except Exception as e:
            raise TelegramBotError(e)

    def send_message(
        self,
        text: str,
        chat_id: int | str,
        **kwargs
    ) -> dict:
        """
        Send a message to a chat.

        Args:
            text (str): The message text to send.
            chat_id (int | str): Unique identifier for the target chat.
            **kwargs: Additional parameters for the Telegram API.

        Returns:
            dict: The sent message as returned by the Telegram API.

        Raises:
            TelegramBotError: If the request fails.
        """
        data = {"text": text, "chat_id": chat_id, **kwargs}

        # Send sendMessage request
        try:
            response = requests.post(self._api_endpoint + "/sendMessage", data=data)
            response.raise_for_status()
        except Exception as e:
            raise TelegramBotError(e)

        return response.json()

    def edit_message(
        self,
        text: str,
        chat_id: int | str,
        message_id: int,
        **kwargs
    ) -> dict:
        """
        Edit an existing message.

        Args:
            text (str): New text of the message.
            chat_id (int | str): Unique identifier for the target chat.
            message_id (int): Identifier of the message to edit.
            **kwargs: Additional parameters for the Telegram API.

        Returns:
            dict: The edited message as returned by the Telegram API.

        Raises:
            TelegramBotError: If the request fails.
        """
        data = {"text": text, "chat_id": chat_id, "message_id": message_id, **kwargs}

        try:
            response = requests.post(self._api_endpoint + "/editMessageText", data=data)
            response.raise_for_status()
        except Exception as e:
            raise TelegramBotError(e)

        return response.json()
        
    def start_loop(self, *callbacks, interval: float = 1.0) -> None:
        """
        Continuously call provided callback functions at a set interval.

        Args:
            *callbacks: Functions to be called in each loop iteration.
            interval (float, optional): Time in seconds to wait between iterations. Default is 1.0.

        KeyboardInterrupt:
            Stops the loop when CTRL+C is pressed.
        """
        import time

        print("Press CTRL+C to exit loop.")
        try:
            while True:
                for func in callbacks:
                    func()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Loop stopped by user.")
