import requests
from config import API_KEY

def upload_video(file_path):
    url = f'https://doodapi.com/api/upload/server?key={API_KEY}'
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    response.raise_for_status()
    return response.json()
