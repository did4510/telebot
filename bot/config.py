import os

# Bot token from BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN", "your-bot-token-here")

# List of paid users
PAID_USERS = os.getenv("PAID_USERS", "").split(",")

# Storage paths
IMAGE_STORAGE = "uploads/images/"
VIDEO_STORAGE = "uploads/videos/"

# Create directories if they don't exist
os.makedirs(IMAGE_STORAGE, exist_ok=True)
os.makedirs(VIDEO_STORAGE, exist_ok=True)

# PayPal configuration
PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID", "your-paypal-client-id")
PAYPAL_CLIENT_SECRET = os.getenv("PAYPAL_CLIENT_SECRET", "your-paypal-client-secret")

# Razorpay configuration
RAZORPAY_API_KEY = os.getenv("RAZORPAY_API_KEY", "your-razorpay-api-key")
RAZORPAY_API_SECRET = os.getenv("RAZORPAY_API_SECRET", "your-razorpay-api-secret")

# Supported payment methods
PAYMENT_METHODS = ["paypal", "upi", "card"]
