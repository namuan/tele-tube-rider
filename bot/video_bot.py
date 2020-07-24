from telegram.ext import Updater

from config import bot_cfg


class VideoBot:
    def __init__(self):
        self.bot_token = bot_cfg("TELEGRAM_BOT_TOKEN")
        self.updater = Updater(token=self.bot_token, use_context=True)
        self.dispatcher = self.updater.dispatcher


bot = VideoBot()
updater = bot.updater
dispatcher = bot.dispatcher
