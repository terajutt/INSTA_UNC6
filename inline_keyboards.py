"""
Inline keyboard layouts for the bot.
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    """Get the main menu inline keyboard."""
    keyboard = [
        [
            InlineKeyboardButton("🎮 Entertainment", callback_data="entertainment_menu"),
            InlineKeyboardButton("🛠️ Utilities", callback_data="utilities_menu")
        ],
        [
            InlineKeyboardButton("📊 Information", callback_data="information_menu")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_entertainment_keyboard() -> InlineKeyboardMarkup:
    """Get the entertainment menu inline keyboard."""
    keyboard = [
        [
            InlineKeyboardButton("😂 Random Joke", callback_data="entertainment_joke"),
            InlineKeyboardButton("💭 Inspirational Quote", callback_data="entertainment_quote")
        ],
        [
            InlineKeyboardButton("🎲 Number Game", callback_data="entertainment_game"),
            InlineKeyboardButton("🧠 Fun Fact", callback_data="entertainment_fact")
        ],
        [
            InlineKeyboardButton("🤔 Riddle", callback_data="entertainment_riddle")
        ],
        [
            InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_utilities_keyboard() -> InlineKeyboardMarkup:
    """Get the utilities menu inline keyboard."""
    keyboard = [
        [
            InlineKeyboardButton("🧮 Calculator", callback_data="utilities_calculator"),
            InlineKeyboardButton("🔄 Unit Converter", callback_data="utilities_converter")
        ],
        [
            InlineKeyboardButton("🔐 Password Generator", callback_data="utilities_password"),
            InlineKeyboardButton("📱 QR Code", callback_data="utilities_qr")
        ],
        [
            InlineKeyboardButton("🔗 URL Shortener", callback_data="utilities_url")
        ],
        [
            InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_information_keyboard() -> InlineKeyboardMarkup:
    """Get the information menu inline keyboard."""
    keyboard = [
        [
            InlineKeyboardButton("🌤️ Weather", callback_data="information_weather"),
            InlineKeyboardButton("📰 News", callback_data="information_news")
        ],
        [
            InlineKeyboardButton("📚 Wikipedia", callback_data="information_wiki"),
            InlineKeyboardButton("💰 Crypto Prices", callback_data="information_crypto")
        ],
        [
            InlineKeyboardButton("🌍 World Time", callback_data="information_time")
        ],
        [
            InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_back_keyboard() -> InlineKeyboardMarkup:
    """Get a simple back to main menu keyboard."""
    keyboard = [
        [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_navigation_keyboard(current_menu: str) -> InlineKeyboardMarkup:
    """Get navigation keyboard for specific menu."""
    if current_menu == "entertainment":
        return get_entertainment_keyboard()
    elif current_menu == "utilities":
        return get_utilities_keyboard()
    elif current_menu == "information":
        return get_information_keyboard()
    else:
        return get_main_menu_keyboard()