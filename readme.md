# 📈 Telegram Stock Alerts Bot

A Python-based Telegram bot for managing stock price alerts 📊, using Yahoo Finance data (via the `yfinance` library) to track stocks and notify users when their desired price thresholds or moving averages are crossed.

<img src="telegram-stock-alerts.gif" alt="Bot Usage" width="600"/>

## ✨ Features

- **Add Alerts**: Users can set alerts for specific stock tickers when the stock reaches a particular price level, percentage change, or moving average (e.g., MA100).
- **Delete Alerts**: Users can easily remove alerts they no longer need.
- **Show All Alerts**: Displays a list of all active alerts for the user, formatted with relevant stock and price data.
- **Automatic Price Checks**: A background process periodically checks stock prices and triggers alerts when conditions are met 🔔.
- **Alert Types**:
  - Price Level Alerts (e.g., when a stock crosses a specific price).
  - Percentage Alerts (e.g., 5% above or below the current price).
  - Moving Average Alerts (e.g., 100-day moving average).

## 🗂 Project Structure

- `bot.py`: Contains the core logic of the Telegram bot 🤖. Handles user interactions like adding, deleting, and showing alerts, as well as validating stock tickers and price data.
- `check_alerts.py`: A script that checks stock price data against user-set alerts and notifies users when conditions are met.
- `database.py`: Manages SQLite database operations to store and retrieve alerts and chat information 🗄.
- `logger_config.py`: Sets up logging for the project, writing events and errors to a log file 📝.
- `requirements.txt`: Lists the Python packages required to run the project.
- `.gitignore`: Ignores sensitive files such as the Telegram bot token, logs, and the database file.

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kemaldahha/telegram-stock-alerts.git
   ```

2. Navigate to the project directory:
   ```bash
   cd telegram-stock-alerts
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a constants.py file with the following content:
   ```bash
   TELEGRAM_TOKEN = 'your_telegram_bot_token_here'
   ```
   Replace `your_telegram_bot_token_here` with your actual Telegram bot token.

```bash
   sudo nano /etc/systemd/system/tsa_bot.service
   
   sudo systemctl daemon-reload
   sudo systemctl enable tsa_bot.service
   sudo systemctl start tsa_bot.service
   sudo systemctl restart tsa_bot.service
```

```bash
crontab -e
0 * * * * /usr/bin/python3 /home/ubuntu/TSA/alert_worker.py >> /home/ubuntu/TSA/cron.log 2>&1
```