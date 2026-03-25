import yt_dlp
from config import DOWNLOAD_PATH

def descargar_audio(url):
    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': f'{DOWNLOAD_PATH}audio.%(ext)s',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return f"{DOWNLOAD_PATH}audio.mp3"