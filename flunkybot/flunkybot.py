"""A bot which checks if there is a new record in the server section of hetzner."""
import logging
from telegram.ext import (
    Filters,
    CommandHandler,
    CallbackQueryHandler,
    ChosenInlineResultHandler,
    InlineQueryHandler,
    MessageHandler,
    Updater,
)

from flunkybot.config import config
# from flunkybot.helper.session import session_wrapper
from flunkybot.helper.telegram import call_tg_func


def start(bot, update):
    """Send a help text."""
    print(update)


def send_help_text(bot, update):
    """Send a help text."""


logging.basicConfig(level=config.LOG_LEVEL,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Initialize telegram updater and dispatcher
updater = Updater(
    token=config.TELEGRAM_API_KEY,
    workers=config.WORKER_COUNT,
    request_kwargs={'read_timeout': 20, 'connect_timeout': 20}
)

dispatcher = updater.dispatcher
# Create message handler
dispatcher.add_handler(CommandHandler('start', start))

# Regular tasks
job_queue = updater.job_queue
