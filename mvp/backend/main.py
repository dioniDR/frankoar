from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

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
    "contenido": "En esta plaza nació el espíritu revolucionario de América del Sur..."
}

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
    respuesta = "Buena pregunta. Soy un personaje histórico vinculado a este lugar." if pregunta else "¿Qué deseas saber?"
    return JSONResponse(content={"pregunta": pregunta, "respuesta": respuesta})
