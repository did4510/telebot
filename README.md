# Telegram Video Upload Bot

This is a Telegram bot that allows users to upload images and videos to selected channels, with support for multiple video resolutions. The bot also differentiates between paid and free users.

## Features
- Select a channel to post content
- Upload images and videos
- Video resolution options (480p, 720p, 1080p)
- 1080p videos available only for paid users

## Setup

### Prerequisites
- Python 3.x
- Telegram Bot Token (from BotFather)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/did4510/telebot
    cd telebot
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure the bot by setting environment variables or editing `config.py`:
    ```bash
    export BOT_TOKEN='your-telegram-bot-token'
    export PAID_USERS='user1,user2,user3'
    export PAYPAL_CLIENT_ID='your-paypal-client-id'
    export PAYPAL_CLIENT_SECRET='your-paypal-client-secret'
    export RAZORPAY_API_KEY='your-razorpay-api-key'
    export RAZORPAY_API_SECRET='your-razorpay-api-secret'
    ```

4. Run the bot:
    ```bash
    python main.py
    ```

### Usage
- `/start` - Start the bot
- `/select` - Select a channel to post to
- `/post` - Enter a post title
- `/image` - Upload an image
- `/upload` - Upload a video (with resolution options)
- `/pay paypal` - Start a PayPal payment
- `/pay upi` - Start a UPI payment via Razorpay
- `/verify <payment_id> <signature> <order_id>` - Verify the payment (Razorpay only)

## License
This project is licensed under the MIT License.
