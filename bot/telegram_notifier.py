class TelegramNotifier:
    def __init__(self, bot, chat_id, update_message_id):
        self.bot = bot
        self.chat_id = chat_id
        self.update_message_id = update_message_id

    def progress_update(self, update_message):
        self.bot.edit_message_text(
            update_message,
            self.chat_id,
            self.update_message_id,
            disable_web_page_preview=True,
        )
