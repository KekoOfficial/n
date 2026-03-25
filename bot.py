from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

from config import TOKEN
from core.queue_system import agregar_tarea
from modules.downloader.video import descargar_video
from modules.downloader.audio import descargar_audio
from modules.downloader.splitter import cortar_video
from utils.cleaner import limpiar

async def comandos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.split()

    if len(texto) < 2:
        await update.message.reply_text("❌ Uso:\n/mp3 link\n/mp4 link [5 o 10]")
        return

    comando = texto[0]
    link = texto[1]
    opcion = texto[2] if len(texto) == 3 else None

    await update.message.reply_text("📥 Añadido a la cola...")

    async def tarea():
        try:
            # 🎵 MP3
            if comando == "/mp3":
                await update.message.reply_text("🎵 Procesando audio...")
                audio = descargar_audio(link)
                await update.message.reply_audio(audio=open(audio, "rb"))
                limpiar(audio)

            # 🎬 MP4
            elif comando == "/mp4":
                await update.message.reply_text("🎬 Descargando completo...")
                video = descargar_video(link)

                if not opcion:
                    await update.message.reply_video(video=open(video, "rb"))
                    limpiar(video)

                else:
                    minutos = int(opcion)

                    if minutos not in [5, 10]:
                        await update.message.reply_text("❌ Solo 5 o 10 minutos")
                        return

                    await update.message.reply_text(f"✂️ Cortando {minutos} min...")

                    partes = cortar_video(video, minutos * 60)

                    for i, parte in enumerate(partes):
                        await update.message.reply_video(
                            video=open(parte, "rb"),
                            caption=f"📦 Parte {i+1}/{len(partes)}"
                        )
                        limpiar(parte)

                    limpiar(video)

        except Exception as e:
            await update.message.reply_text(f"❌ Error: {str(e)}")

    await agregar_tarea(tarea)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, comandos))
    app.add_handler(MessageHandler(filters.COMMAND, comandos))

    import asyncio
    from core.worker import worker

    loop = asyncio.get_event_loop()
    loop.create_task(worker())  # 🔥 worker activo

    print("👑 KHASAM IMPERIO ACTIVO")
    app.run_polling()

if __name__ == "__main__":
    main()