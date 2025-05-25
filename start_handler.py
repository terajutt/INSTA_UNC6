"""
Handler for start and help commands.
"""

from telegram import Update
from telegram.ext import ContextTypes
from inline_keyboards import get_main_menu_keyboard
from logger import get_logger
from user_state import UserStateManager

logger = get_logger(__name__)
user_state = UserStateManager()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command and show main menu."""
    user = update.effective_user
    chat_id = update.effective_chat.id
    
    logger.info(f"User {user.id} ({user.username}) started the bot")
    
    # Initialize user state
    user_state.initialize_user(user.id)
    
    welcome_message = (
        f"🎉✨ **Welcome {user.first_name}!** ✨🎉\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🤖 **I'm your AI-powered assistant!**\n"
        f"🌟 Ready to help you with amazing features:\n\n"
        f"🎮 **🎯 Entertainment Hub**\n"
        f"   ┣ 😂 Jokes & Quotes\n"
        f"   ┣ 🎲 Interactive Games\n"
        f"   ┗ 🧠 Brain Teasers\n\n"
        f"🛠️ **⚡ Utility Toolbox**\n"
        f"   ┣ 🧮 Smart Calculator\n"
        f"   ┣ 🔄 Unit Converter\n"
        f"   ┣ 🔐 Password Generator\n"
        f"   ┗ 📱 QR Code Magic\n\n"
        f"📊 **🌍 Information Center**\n"
        f"   ┣ 🌤️ Live Weather\n"
        f"   ┣ 📰 Breaking News\n"
        f"   ┣ 📚 Wikipedia Search\n"
        f"   ┗ 💰 Crypto Prices\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"💡 **Pro Tip:** Use buttons OR type commands!\n"
        f"🚀 **Let's explore together!**"
    )
    
    try:
        await update.message.reply_text(
            welcome_message,
            reply_markup=get_main_menu_keyboard(),
            parse_mode='Markdown'
        )
    except Exception as e:
        logger.error(f"Error in start command: {e}")
        await update.message.reply_text(
            "Sorry, I encountered an error. Please try again with /start"
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /help command."""
    help_text = (
        "🆘 **✨ Ultimate Bot Guide ✨**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🎯 **Quick Commands:**\n"
        "┣ `/start` - 🏠 Main menu\n"
        "┣ `/help` - 🆘 This guide\n"
        "┗ `/menu` - 🔄 Return home\n\n"
        "🎮 **Navigation Magic:**\n"
        "┣ 🔘 Use beautiful buttons below\n"
        "┣ 💬 Type commands directly\n"
        "┣ 🔙 'Back' buttons for easy navigation\n"
        "┗ 🧠 I remember your journey!\n\n"
        "🌟 **Feature Universe:**\n"
        "┣ 🎮 **Entertainment** - Fun & games\n"
        "┣ 🛠️ **Utilities** - Power tools\n"
        "┗ 📊 **Information** - Live data\n\n"
        "🆘 **Need Help?** Use `/start` to reset\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "💡 **Ready to explore? Let's go!**"
    )
    
    try:
        await update.message.reply_text(
            help_text,
            reply_markup=get_main_menu_keyboard(),
            parse_mode='Markdown'
        )
    except Exception as e:
        logger.error(f"Error in help command: {e}")
        await update.message.reply_text("Error displaying help. Please try /start")