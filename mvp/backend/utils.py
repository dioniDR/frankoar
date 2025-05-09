import os
import json
from dotenv import load_dotenv

def cargar_personaje(nombre_archivo="miranda.json"):
    ruta = f"content/personajes/{nombre_archivo}"
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def cargar_clave_openai():
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")
