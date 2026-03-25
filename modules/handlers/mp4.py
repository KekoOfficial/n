COMMAND = "/mp4"

from modules.downloader.video import descargar_video
from modules.downloader.splitter import cortar_video
from utils.cleaner import limpiar

async def handle(update, context, texto):
    try:
        link = texto[1]
        opcion = texto[2] if len(texto) == 3 else None

        await update.message.reply_text("🎬 Descargando video completo...")
        video = descargar_video(link)

        # 🔥 1. ENVIAR VIDEO COMPLETO
        await update.message.reply_video(video=open(video, "rb"))

        if not opcion:
            limpiar(video)
            return

        minutos = int(opcion)
        if minutos not in [5, 10]:
            await update.message.reply_text("❌ Solo 5 o 10 minutos")
            limpiar(video)
            return

        await update.message.reply_text(f"✂️ Recortando en {minutos} minutos...")
        partes = cortar_video(video, minutos * 60)

        for i, parte in enumerate(partes):
            await update.message.reply_video(video=open(parte, "rb"),
                                             caption=f"📦 Parte {i+1}/{len(partes)}")
            limpiar(parte)

        limpiar(video)

    except Exception as e:
        await update.message.reply_text(f"❌ Error MP4: {str(e)}")