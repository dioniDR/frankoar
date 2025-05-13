from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import re

# Importar los módulos
from utils import (
    listar_personajes, 
    cargar_personaje, 
    personajes_cercanos,
    respuesta_basada_en_keyword
)
from openai_conn import responder_con_openai

# Crear directorios necesarios
for path in ["static", "static/avatares", "content/personajes", "content/qa"]:
    os.makedirs(path, exist_ok=True)

app = FastAPI(
    title="FRANKO.AR API",
    description="API para el proyecto FRANKO.AR de realidad aumentada con personajes históricos",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción se limitaría a dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar carpeta de imágenes estáticas
app.mount("/static", StaticFiles(directory="static"), name="static")

# Modelos de datos
class Consulta(BaseModel):
    pregunta: str
    personaje_id: str = None

class CoordenadaConsulta(BaseModel):
    lat: float
    lng: float
    radio: float = 10.0  # Radio en kilómetros

# Endpoints
@app.get("/")
async def root():
    """Punto de entrada para verificar que la API está funcionando."""
    return {
        "proyecto": "FRANKO.AR",
        "estado": "activo",
        "endpoints": [
            {"ruta": "/personajes", "descripcion": "Lista todos los personajes disponibles"},
            {"ruta": "/personaje/{id}", "descripcion": "Información detallada de un personaje específico"},
            {"ruta": "/personajes_cercanos", "descripcion": "Encuentra personajes cercanos a una ubicación"},
            {"ruta": "/preguntar", "descripcion": "Envía preguntas a un personaje (básico)"},
            {"ruta": "/consultar", "descripcion": "Envía preguntas a un personaje (IA avanzada)"}
        ]
    }

@app.get("/personajes")
async def get_personajes():
    """Lista todos los personajes disponibles en el sistema."""
    return listar_personajes()

@app.get("/personaje/{personaje_id}")
async def get_personaje(personaje_id: str = None):
    """Obtiene la información detallada de un personaje específico."""
    personaje = cargar_personaje(personaje_id)
    if "error" in personaje:
        raise HTTPException(status_code=404, detail="Personaje no encontrado")
    return personaje

@app.post("/personajes_cercanos")
async def get_personajes_cercanos(coordenadas: CoordenadaConsulta):
    """
    Encuentra personajes históricos cercanos a las coordenadas proporcionadas.
    
    Args:
        lat (float): Latitud
        lng (float): Longitud
        radio (float, opcional): Radio de búsqueda en kilómetros (default: 10km)
    
    Returns:
        list: Personajes ordenados por proximidad
    """
    try:
        cercanos = personajes_cercanos(
            coordenadas.lat, 
            coordenadas.lng, 
            coordenadas.radio
        )
        
        # Simplificar la respuesta para no enviar todos los datos
        return [
            {
                "id": p["id"],
                "nombre": p["nombre"],
                "frase": p["frase"],
                "distancia": round(p["distancia"], 2),
                "lugar": p.get("lugar_relacionado", p.get("ubicacion", {}).get("lugar", ""))
            }
            for p in cercanos
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar personajes cercanos: {str(e)}")

@app.get("/avatar")
async def get_avatar(personaje_id: str = Query(None, description="ID del personaje a consultar")):
    """Obtiene la información del avatar para presentarlo en AR."""
    personaje = cargar_personaje(personaje_id)
    if "error" in personaje:
        raise HTTPException(status_code=404, detail="Personaje no encontrado")

    # Crear la información del avatar
    avatar_info = {
        "id": personaje["id"],
        "nombre": personaje.get("nombre", "Personaje Histórico"),
        "frase": personaje.get("frase", ""),
        "imagen": "/static/avatar.png",  # Imagen por defecto
        "ubicacion": personaje.get("ubicacion", {
            "lat": 0,
            "lng": 0,
            "lugar": "Ubicación desconocida"
        })
    }  # Properly closed dictionary

    return avatar_info

# Fixing the unresolved import
# Ensure the utils module exists and is in the correct path. If not, provide the correct path or create the module.