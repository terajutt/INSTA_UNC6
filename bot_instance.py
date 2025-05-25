"""
Bot instance creation and handler registration.
"""

from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from start_handler import start_command, help_command
from menu_handler import main_menu_callback, back_to_main_callback, navigation_callback
from entertainment_handler import entertainment_callback
from utilities_handler import utilities_callback
from information_handler import information_callback
from text_handler import handle_text_message
from logger import get_logger

logger = get_logger(__name__)

def create_bot(token: str) -> Application:
    """
    Create and configure the bot application with all handlers.
    
    Args:
        token (str): Telegram bot token
        
    Returns:
        Application: Configured bot application
    """
    # Create application
    application = Application.builder().token(token).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("menu", start_command))
    
    # Add callback query handlers
    application.add_handler(CallbackQueryHandler(main_menu_callback, pattern="^main_menu$"))
    application.add_handler(CallbackQueryHandler(back_to_main_callback, pattern="^back_to_main$"))
    application.add_handler(CallbackQueryHandler(navigation_callback, pattern="^nav_"))
    
    # Add feature handlers
    application.add_handler(CallbackQueryHandler(entertainment_callback, pattern="^entertainment"))
    application.add_handler(CallbackQueryHandler(utilities_callback, pattern="^utilities"))
    application.add_handler(CallbackQueryHandler(information_callback, pattern="^information"))
    
    # Add text message handler (should be last)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))
    
    logger.info("Bot application created and handlers registered")
    return application