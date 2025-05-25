"""
Configuration settings for the Telegram bot.
"""

import os

# Bot configuration
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7785363595:AAGARQXzqWyf_Ix0Q2hBUco9FKCvV35rPpQ")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "")

# Feature toggles
ENABLE_ENTERTAINMENT = True
ENABLE_UTILITIES = True
ENABLE_INFORMATION = True

# External API configurations
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")

# Bot settings
MAX_MESSAGE_LENGTH = 4096
CACHE_TIMEOUT = 300  # 5 minutes
USER_STATE_TIMEOUT = 1800  # 30 minutes

# Logging configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
