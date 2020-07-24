#!/usr/bin/python3
"""
python3 main.py
"""
from telegram.ext import CommandHandler

from bot import *
from bot.generic_message_handler import GenericMessageHandler
from bot.video_bot import dispatcher, updater
from config import init_logger

if __name__ == "__main__":
    init_logger()
    dispatcher.add_error_handler(handle_telegram_error)

    # Add command handlers to dispatcher
    dispatcher.add_handler(CommandHandler("start", start_cmd))
    dispatcher.add_handler(CommandHandler("restart", restart_cmd, pass_chat_data=True))
    dispatcher.add_handler(
        CommandHandler("shutdown", shutdown_cmd, pass_chat_data=True)
    )

    # Register message handler
    GenericMessageHandler(dispatcher)

    updater.start_polling()

    updater.idle()
