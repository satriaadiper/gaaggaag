# main.py

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import downloader
import uploader
from config import TELEGRAM_BOT_TOKEN

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Hi! I can download and upload videos for you.')

def handle_video(update, context):
    file_id = update.message.video.file_id
    file_path = downloader.download_video(file_id)
    file_info = uploader.upload_video(file_path)

    if file_info:
        update.message.reply_text(f"Video uploaded! Filecode: {file_info['filecode']}")
    else:
        update.message.reply_text("Error uploading video")

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.video, handle_video))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
