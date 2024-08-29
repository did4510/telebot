from telegram import Update
from telegram.ext import CallbackContext

from bot.config import IMAGE_STORAGE, VIDEO_STORAGE, PAID_USERS
from bot.payments import create_paypal_payment, create_razorpay_payment, verify_razorpay_payment

user_data = {}

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! Use /select to choose a channel.")

def select_channel(update: Update, context: CallbackContext):
    update.message.reply_text("Please enter the channel name:")
    return "POST_TITLE"

def post_title(update: Update, context: CallbackContext):
    user_data['channel'] = update.message.text
    update.message.reply_text("Channel selected. Now, send the post title with /post")
    return "IMAGE_UPLOAD"

def upload_image(update: Update, context: CallbackContext):
    photo_file = update.message.photo[-1].get_file()
    user_data['post_title'] = update.message.caption or 'default_post_title'
    photo_file.download(f"{IMAGE_STORAGE}{user_data['post_title']}_image.jpg")
    update.message.reply_text("Image uploaded! Now, upload a video with /upload")
    return "VIDEO_UPLOAD"

def video_upload(update: Update, context: CallbackContext):
    video_file = update.message.video.get_file()
    video_file.download(f"{VIDEO_STORAGE}{user_data['post_title']}_video.mp4")

    update.message.reply_text("Video uploaded and processed! Choose a quality when you download or stream.")
    return "END"

def start_payment(update: Update, context: CallbackContext):
    user = update.message.from_user
    if context.args and context.args[0] == "paypal":
        payment = create_paypal_payment(amount=10.0)  # Example amount
        if payment:
            update.message.reply_text(f"Please complete the payment: {payment['links'][1]['href']}")
        else:
            update.message.reply_text("Payment failed. Please try again.")
    elif context.args and context.args[0] == "upi":
        order = create_razorpay_payment(amount=10.0)  # Example amount
        update.message.reply_text(f"Pay via UPI: {order['id']}")
    else:
        update.message.reply_text("Please choose a valid payment method: /pay paypal or /pay upi")

def verify_payment(update: Update, context: CallbackContext):
    payment_id = context.args[0]
    signature = context.args[1]
    order_id = context.args[2]
    
    if verify_razorpay_payment(payment_id, signature, order_id):
        update.message.reply_text("Payment successful!")
        # Mark user as paid in your database
    else:
        update.message.reply_text("Payment verification failed. Please try again.")

def cancel(update: Update, context: CallbackContext):
    update.message.reply_text('Operation cancelled.')
    return "END"
