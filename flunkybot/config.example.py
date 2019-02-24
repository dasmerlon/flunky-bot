"""Config values for flunkybot."""
import logging


class Config:
    """Config class for convenient configuration."""

    # Get your telegram api-key from @botfather
    TELEGRAM_API_KEY = None
    SQL_URI = 'sqlite:///flunkybot.db'
    SENTRY_TOKEN = None
    LOG_LEVEL = logging.INFO
    DEBUG = False

    # Performance/thread/db settings
    WORKER_COUNT = 16

    # Use and configure nginx webhooks
    WEB_HOOK = False
    Domain = "https://localhost"
    TOKEN = "flunky_bot"
    PORT = 7000


config = Config()
