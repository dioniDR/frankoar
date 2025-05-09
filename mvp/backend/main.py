from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción se limitaría a dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Datos simulados
avatar_info = {
    "nombre": "Francisco Miranda",
    "ubicacion": {
        "lat": -34.6037,
        "lng": -58.3816,
        "lugar": "Plaza de Mayo"
    },
    "imagen": "/static/avatar.png"
}

historia = {
    "titulo": "El inicio de una revolución",
    "contenido": "En esta plaza nació el espíritu revolucionario de América del Sur. Aquí se reunieron los patriotas que soñaban con una nación libre e independiente."
}

# Crear directorio de static si no existe
os.makedirs("static", exist_ok=True)

# Montar carpeta de imágenes estáticas
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/avatar")
async def get_avatar():
    return avatar_info

@app.get("/historia")
async def get_historia():
    return historia

@app.post("/preguntar")
async def preguntar(request: Request):
    data = await request.json()
    pregunta = data.get("pregunta", "")
    
    # Sistema básico de respuestas basado en palabras clave
    respuesta = "No tengo información sobre eso en mis registros históricos."
    
    if not pregunta:
        respuesta = "¿Qué deseas saber sobre la historia de este lugar?"
    elif "quien" in pregunta.lower() or "quién" in pregunta.lower():
        respuesta = "Soy Francisco Miranda, uno de los precursores de la independencia en América Latina."
    elif "revolución" in pregunta.lower() or "independencia" in pregunta.lower():
        respuesta = "La revolución comenzó como un movimiento de ideas que luego se transformó en acción. Muchos de los primeros pasos se dieron justo aquí, donde estamos ahora."
    elif "plaza" in pregunta.lower() or "lugar" in pregunta.lower():
        respuesta = "Esta plaza ha sido testigo de momentos cruciales en nuestra historia. Aquí se han reunido patriotas, se han declarado independencias y se ha celebrado la libertad."
    
    return JSONResponse(content={"pregunta": pregunta, "respuesta": respuesta})

# Agregar una ruta de salud para verificar que el servidor está funcionando
@app.get("/")
async def root():
    return {"mensaje": "API de FRANKO.AR funcionando correctamente"}
