# 🤖 SMARTMATE BOT

A feature-rich Telegram bot with beautiful UI and multiple interactive capabilities including entertainment, utilities, and information services.

## ✨ Features

### 🎮 Entertainment
- 😂 Random jokes with beautiful styling
- 💭 Inspirational quotes
- 🎲 Number guessing games
- 🧠 Fun facts
- 🤔 Brain teaser riddles

### 🛠️ Utilities
- 🧮 Mathematical calculator
- 🔄 Unit converter (length, weight, temperature)
- 🔐 Secure password generator
- 📱 QR code generator
- 🔗 URL shortener information
- 🔤 Text encoding/decoding (Base64, URL, HTML)

### 📊 Information
- 🌤️ Weather information
- 📰 Latest news headlines
- 🔍 Wikipedia search
- 💰 Cryptocurrency prices
- 🌍 World time information
- 💱 Currency exchange rates

## 🚀 Deployment on Render

### Prerequisites
- Render account
- Telegram Bot Token from @BotFather

### Deploy Steps

1. **Fork or Upload this repository to GitHub**

2. **Create a new Web Service on Render:**
   - Connect your GitHub repository
   - Choose "Worker" as service type
   - Use the following settings:
     - **Name:** `smartmate-bot`
     - **Environment:** `Python 3`
     - **Build Command:** `pip install -r render_requirements.txt`
     - **Start Command:** `python main.py`

3. **Set Environment Variables:**
   - `TELEGRAM_BOT_TOKEN`: Your bot token from @BotFather
   - `WEATHER_API_KEY`: (Optional) OpenWeatherMap API key
   - `NEWS_API_KEY`: (Optional) NewsAPI key

4. **Deploy:**
   - Click "Create Web Service"
   - Wait for deployment to complete

### Alternative: Manual Deployment

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd smartmate-bot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r render_requirements.txt
   ```

3. **Set environment variables:**
   ```bash
   export TELEGRAM_BOT_TOKEN="your_bot_token_here"
   ```

4. **Run the bot:**
   ```bash
   python main.py
   ```

## 🎨 Bot Interface

The bot features a stunning visual interface with:
- Unicode separators and borders
- Emoji-rich menus
- Professional gradients and styling
- Inline keyboard navigation
- Beautiful response formatting

## 📱 Usage

1. Start a chat with your bot on Telegram
2. Send `/start` to see the main menu
3. Navigate using inline buttons or send direct commands:
   - `wiki search term` - Search Wikipedia
   - `weather city name` - Get weather info
   - `calc 2+2*3` - Calculate expressions
   - Numbers for guessing game

## 🔧 Configuration

### Required Environment Variables
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token

### Optional Environment Variables
- `WEATHER_API_KEY`: For weather services
- `NEWS_API_KEY`: For news headlines
- `LOG_LEVEL`: Logging level (default: INFO)

## 📂 Project Structure

```
smartmate-bot/
├── bot/
│   ├── features/          # Bot feature implementations
│   ├── handlers/          # Message and callback handlers
│   ├── keyboards/         # Inline keyboard layouts
│   ├── utils/            # Utility functions
│   └── bot_instance.py   # Bot initialization
├── main.py               # Entry point
├── config.py            # Configuration settings
├── render_requirements.txt  # Dependencies
├── Procfile             # Process definition
├── render.yaml          # Render configuration
└── smartmate_bot_logo.svg  # Bot logo
```

## 🎯 API Keys (Optional)

To unlock full functionality, obtain these free API keys:

1. **Weather Services:**
   - Get free API key from [OpenWeatherMap](https://openweathermap.org/api)
   - Add as `WEATHER_API_KEY` environment variable

2. **News Services:**
   - Get free API key from [NewsAPI](https://newsapi.org/)
   - Add as `NEWS_API_KEY` environment variable

## 🛡️ Security

- Bot token is stored securely in environment variables
- No sensitive data is logged
- All external API calls are handled safely

## 📊 Monitoring

The bot includes comprehensive logging for:
- User interactions
- Feature usage
- Error tracking
- Performance monitoring

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

This project is open source and available under the MIT License.

---

**Enjoy your SMARTMATE BOT! 🚀**