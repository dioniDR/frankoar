import os
import time
import requests
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
API_URL = "http://localhost:8000/preguntar"  # Cambia si usas otra URL

# Simulación por defecto
modo_simulado = False

if not API_KEY:
    print("[⚠️] Clave OPENAI_API_KEY no encontrada en .env → modo simulado activado.")
    modo_simulado = True

# Datos para la prueba
pregunta = "¿Cuál es el propósito del proyecto FRANKO.AR?"

if modo_simulado:
    # Modo sin conexión real
    respuesta = {
        "respuesta": "Este es un mensaje simulado. El sistema no tiene acceso real a la API."
    }
    tiempo_respuesta = 0
else:
    try:
        inicio = time.time()
        response = requests.post(API_URL, json={"pregunta": pregunta}, headers={"Authorization": f"Bearer {API_KEY}"})
        tiempo_respuesta = round(time.time() - inicio, 2)

        if response.status_code == 200:
            respuesta = response.json()
        else:
            print(f"[❌] Error HTTP {response.status_code}")
            respuesta = {}
    except Exception as e:
        print(f"[⚠️] Error en la llamada a la API: {e}")
        respuesta = {}
        modo_simulado = True

# Resultados
print("\n--- RESULTADO PRUEBA /preguntar ---")
print(f"Tiempo de respuesta: {tiempo_respuesta}s")
print(f"Mensaje recibido: {respuesta}")
print("¿Contiene clave 'respuesta'? →", 'respuesta' in respuesta)

# Validación de contenido
if "respuesta" in respuesta:
    contenido = respuesta["respuesta"].strip().lower()
    if contenido and contenido not in ["no sé", "no tengo respuesta", "respuesta genérica"]:
        print("[✅] Respuesta válida.")
    else:
        print("[⚠️] Respuesta vacía o genérica.")
else:
    print("[❌] No se recibió una clave 'respuesta'.")
