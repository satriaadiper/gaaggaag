from telegram import Bot
from config import TELEGRAM_BOT_TOKEN
import os

# Initialize the bot using the provided token
bot = Bot(TELEGRAM_BOT_TOKEN)

def download_video(file_id):
    # Define the download path for the video
    file_path = f'downloads/{file_id}.mp4'
    
    # Get the file using the provided file_id
    new_file = bot.get_file(file_id)
    
    # Download the file to the specified path
    new_file.download(file_path)
    
    return file_path
