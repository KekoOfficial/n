import os

def limpiar(path):
    try:
        if os.path.exists(path):
            os.remove(path)
    except:
        pass