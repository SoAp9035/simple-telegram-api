class TelegramBotError(Exception):
    def __init__(self, message: str = "TelegramBot Error"):
        super().__init__(message)
