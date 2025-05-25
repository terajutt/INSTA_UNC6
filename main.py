#!/usr/bin/env python3
"""
Main entry point for the Telegram bot.
This file initializes and starts the bot with all handlers.
"""

import asyncio
import os
import sys
from bot_instance import create_bot
from logger import setup_logging

def main():
    """Main function to start the bot."""
    # Setup logging
    logger = setup_logging()
    
    # Get bot token from environment or use provided token
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "7785363595:AAGARQXzqWyf_Ix0Q2hBUco9FKCvV35rPpQ")
    if not bot_token:
        logger.error("TELEGRAM_BOT_TOKEN environment variable is required!")
        sys.exit(1)
    
    logger.info("Starting Telegram bot...")
    
    try:
        # Create and start the bot
        application = create_bot(bot_token)
        
        # Start the bot
        application.run_polling(drop_pending_updates=True)
        
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
