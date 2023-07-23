import os
from doodstream import DoodStream
from config import API_KEY
import downloader

DOWNLOAD_FOLDER = 'downloads'

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

d = DoodStream()
d.api_key = API_KEY

def upload_video(file_id):
    file_path = os.path.join(DOWNLOAD_FOLDER, f"{file_id}.mp4")

    downloader.download_video(file_id, file_path)

    upload_result = d.local_upload(file_path)

    file_id = upload_result['id']

    file_info = d.file_info(file_id)

    return file_info
