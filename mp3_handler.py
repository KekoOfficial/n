from modules.downloader.audio import descargar_audio
from utils.cleaner import limpiar

async def handle_mp3(update, context, texto):
    try:
        link = texto[1]

        await update.message.reply_text("🎵 Descargando música...")
        audio = descargar_audio(link)

        await update.message.reply_audio(audio=open(audio, "rb"))
        limpiar(audio)

    except Exception as e:
        await update.message.reply_text(f"❌ Error MP3: {str(e)}")