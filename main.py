import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import downloader
import uploader

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define a few command handlers
def start(update, context):
    update.message.reply_text('Hi! I can download and upload videos for you.')

def help(update, context):
    update.message.reply_text('/help - Get help\n/about - About this bot')

def about(update, context):
    update.message.reply_text('I am a bot that can download and upload videos!')

def handle_video(update, context):
    file_id = update.message.video.file_id
    file_path = downloader.download_video(file_id)
    upload_result = uploader.upload_video(file_path)
    update.message.reply_text(f"Video uploaded! Filecode: {upload_result['filecode']}")

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    TELEGRAM_BOT_TOKEN = '6068957387:AAEBNTiYX83G54iaOGl5xPPKPdUsuDnH2mw'
    updater = Updater(TELEGRAM_BOT_TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("about", about))

    dp.add_handler(MessageHandler(Filters.video, handle_video))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
