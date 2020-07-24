import logging

from config import bot_cfg


# Decorator to restrict access if user is not the same as in config
def restrict_access(func):
    def _restrict_access(bot, update, chat_data):
        chat_id = get_chat_id(update)
        if str(chat_id) != bot_cfg("TELEGRAM_USER_ID"):
            # Inform owner of bot
            msg = "Access denied for user %s" % chat_id
            bot.send_message(bot_cfg("TELEGRAM_USER_ID"), text=msg)

            logging.info(msg)
            return
        else:
            return func(bot, update, chat_data)

    return _restrict_access


# Return chat ID for an update object
def get_chat_id(update=None):
    if update.message:
        return update.message.chat_id
    elif update.callback_query:
        return update.callback_query.from_user["id"]


# Handle all telegram and telegram.ext related errors
def handle_telegram_error(update, error):
    error_str = "Update '%s' caused error '%s'" % (update, error)
    logging.error(error_str)
