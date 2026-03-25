import os
import importlib

handlers = {}

def cargar_handlers():
    ruta = "modules.handlers"

    for archivo in os.listdir("modules/handlers"):
        if archivo.endswith(".py") and archivo not in ["loader.py", "__init__.py", "command_handler.py"]:
            nombre = archivo[:-3]
            modulo = importlib.import_module(f"{ruta}.{nombre}")
            if hasattr(modulo, "COMMAND"):
                handlers[modulo.COMMAND] = modulo.handle

def get_handler(cmd):
    return handlers.get(cmd)