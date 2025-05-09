from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from utils import cargar_personaje
from openai_conn import responder_con_openai

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

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
    "contenido": "En esta plaza nació el espíritu revolucionario de América del Sur..."
}

class Consulta(BaseModel):
    pregunta: str

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
    respuesta = "Buena pregunta. Soy un personaje histórico vinculado a este lugar." if pregunta else "¿Qué deseas saber?"
    return JSONResponse(content={"pregunta": pregunta, "respuesta": respuesta})

@app.post("/consultar")
async def consultar(consulta: Consulta):
    if not consulta.pregunta.strip():
        return JSONResponse(content={"error": "Pregunta vacía"}, status_code=400)
    personaje = cargar_personaje()
    respuesta = responder_con_openai(consulta.pregunta, personaje)
    return respuesta
