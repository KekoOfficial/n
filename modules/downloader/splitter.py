import subprocess
import glob
import os
from config import DOWNLOAD_PATH, MAX_PARTS

def cortar_video(input_path, duracion):
    # limpiar partes anteriores
    for f in glob.glob(f"{DOWNLOAD_PATH}parte_*.mp4"):
        os.remove(f)

    output_template = f"{DOWNLOAD_PATH}parte_%03d.mp4"

    cmd = [
        "ffmpeg",
        "-i", input_path,
        "-c", "copy",
        "-map", "0",
        "-segment_time", str(duracion),
        "-f", "segment",
        "-reset_timestamps", "1",
        output_template
    ]

    subprocess.run(cmd)

    partes = sorted(glob.glob(f"{DOWNLOAD_PATH}parte_*.mp4"))
    return partes[:MAX_PARTS]