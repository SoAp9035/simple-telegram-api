import requests

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{self.token}"

    def send_message(self, chat_id, text, reply_to_message=False, message_id=None):
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
        return response.json()
    
    def edit_message(self, chat_id, message_id, text):
        url = f"{self.api_url}/editMessageText"
        data = {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": text
        }
        response = requests.post(url, json=data)
        return response.json()

    def get_updates(self, offset=None, timeout=30):
        url = f"{self.api_url}/getUpdates"
        data = {
            "timeout": timeout,
            "offset": offset
        }
        response = requests.post(url, json=data)
        if not response.json()["result"]:
            return None
        return response.json()
    
    def get_last_message(self):
        updates = self.get_updates()
        if updates:
            last_update = updates["result"][-1]
            chat_id = last_update["message"]["chat"]["id"]
            username = last_update["message"]["from"]["username"]
            message_id = last_update["message"]["message_id"]
            text = last_update["message"]["text"]
            return {"chat_id": chat_id, "username": username, "message_id": message_id, "text": text}
        return None
    
    def reset_updates(self):
        updates = self.get_updates(timeout=1)
        if updates:
            update_id = updates["result"][-1]["update_id"] + 1
            self.get_updates(offset=update_id, timeout=1)
            return update_id
        return None
