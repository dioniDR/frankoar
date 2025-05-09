import os
import json
from dotenv import load_dotenv

# Ruta base: siempre apunta a la carpeta backend
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def cargar_personaje(nombre_archivo="miranda.json"):
    ruta = os.path.join(BASE_DIR, "content", "personajes", nombre_archivo)
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def cargar_clave_openai():
    load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))
    return os.getenv("OPENAI_API_KEY")
