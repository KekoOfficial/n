import yt_dlp
from config import DOWNLOAD_PATH

def descargar_video(url):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': f'{DOWNLOAD_PATH}video.%(ext)s',
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return f"{DOWNLOAD_PATH}video.mp4"