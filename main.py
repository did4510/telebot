from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from bot.config import BOT_TOKEN
from bot.handlers import start, select_channel, post_title, upload_image, video_upload, cancel, start_payment, verify_payment

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('select', select_channel)],
        states={
            "POST_TITLE": [MessageHandler(Filters.text, post_title)],
            "IMAGE_UPLOAD": [MessageHandler(Filters.photo, upload_image)],
            "VIDEO_UPLOAD": [MessageHandler(Filters.video, video_upload)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler("pay", start_payment))
    dp.add_handler(CommandHandler("verify", verify_payment))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
