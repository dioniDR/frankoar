import os
import json
import math
from dotenv import load_dotenv

# Ruta base: siempre apunta a la carpeta backend
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def distancia_haversine(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia entre dos puntos geográficos utilizando la fórmula de Haversine.
    
    Args:
        lat1, lon1: Latitud y longitud del primer punto (en grados)
        lat2, lon2: Latitud y longitud del segundo punto (en grados)
        
    Returns:
        float: Distancia en kilómetros entre los dos puntos
    """
    # Radio de la Tierra en km
    R = 6371.0
    
    # Convertir grados a radianes
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Diferencias
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    # Fórmula de Haversine
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distancia = R * c
    
    return distancia

def listar_personajes():
    """
    Lista todos los personajes disponibles en la carpeta de personajes.
    
    Returns:
        list: Lista de diccionarios con información básica de cada personaje.
    """
    ruta_personajes = os.path.join(BASE_DIR, "content", "personajes")
    personajes = []
    
    # Asegurarse de que la carpeta existe
    if not os.path.exists(ruta_personajes):
        os.makedirs(ruta_personajes, exist_ok=True)
        return personajes
    
    # Recorrer archivos JSON en la carpeta de personajes
    for archivo in os.listdir(ruta_personajes):
        if archivo.endswith('.json'):
            try:
                ruta_completa = os.path.join(ruta_personajes, archivo)
                with open(ruta_completa, "r", encoding="utf-8") as f:
                    datos = json.load(f)
                    # Añadir el nombre del archivo como ID si no existe
                    if "id" not in datos:
                        datos["id"] = archivo.replace('.json', '')
                    # Añadir solo información básica a la lista
                    personajes.append({
                        "id": datos["id"],
                        "nombre": datos.get("nombre", "Sin nombre"),
                        "frase": datos.get("frase", ""),
                        "epoca": datos.get("epoca", "Desconocida")
                    })
            except Exception as e:
                print(f"Error al leer {archivo}: {str(e)}")
    
    return personajes

def personajes_cercanos(lat, lon, max_distancia=10.0):
    """
    Encuentra personajes cercanos a una ubicación geográfica.
    
    Args:
        lat (float): Latitud del usuario
        lon (float): Longitud del usuario
        max_distancia (float): Distancia máxima en kilómetros (default 10 km)
        
    Returns:
        list: Lista de personajes ordenados por cercanía
    """
    todos_personajes = []
    ruta_personajes = os.path.join(BASE_DIR, "content", "personajes")
    
    # Verificar si la carpeta existe
    if not os.path.exists(ruta_personajes):
        return []
    
    # Recorrer cada archivo JSON de personaje
    for archivo in os.listdir(ruta_personajes):
        if archivo.endswith('.json'):
            try:
                ruta_completa = os.path.join(ruta_personajes, archivo)
                with open(ruta_completa, "r", encoding="utf-8") as f:
                    personaje = json.load(f)
                    
                    # Verificar si el personaje tiene ubicación
                    if "ubicacion" in personaje and "lat" in personaje["ubicacion"] and "lng" in personaje["ubicacion"]:
                        # Calcular distancia
                        distancia = distancia_haversine(
                            lat, lon, 
                            personaje["ubicacion"]["lat"], 
                            personaje["ubicacion"]["lng"]
                        )
                        
                        # Añadir solo si está dentro del rango
                        if distancia <= max_distancia:
                            # Añadir distancia al personaje para ordenar
                            personaje["distancia"] = distancia
                            todos_personajes.append(personaje)
                    
                    # Verificar si el personaje tiene lugares relacionados
                    if "lugares_relacionados" in personaje:
                        for lugar in personaje["lugares_relacionados"]:
                            if "lat" in lugar and "lng" in lugar:
                                distancia = distancia_haversine(
                                    lat, lon, 
                                    lugar["lat"], 
                                    lugar["lng"]
                                )
                                
                                # Si un lugar relacionado está cerca, añadir el personaje
                                if distancia <= max_distancia and not any(p["id"] == personaje["id"] for p in todos_personajes):
                                    personaje["distancia"] = distancia
                                    personaje["lugar_relacionado"] = lugar["nombre"]
                                    todos_personajes.append(personaje)
                    
            except Exception as e:
                print(f"Error al procesar personaje {archivo}: {str(e)}")
    
    # Ordenar por distancia
    return sorted(todos_personajes, key=lambda x: x["distancia"])

def cargar_personaje(id_personaje=None):
    """
    Carga un personaje específico por su ID o el primero disponible si no se especifica.
    
    Args:
        id_personaje (str, optional): ID del personaje a cargar. Default None.
        
    Returns:
        dict: Datos del personaje.
    """
    if id_personaje:
        nombre_archivo = f"{id_personaje}.json"
    else:
        # Si no se especifica, usar el predeterminado
        nombre_archivo = "frida_kahlo.json"  # Cambiamos el default a Frida
    
    ruta = os.path.join(BASE_DIR, "content", "personajes", nombre_archivo)
    
    # Verificar si el archivo existe
    if not os.path.exists(ruta):
        # Si no existe, buscar el primero disponible
        personajes = listar_personajes()
        if personajes:
            nombre_archivo = f"{personajes[0]['id']}.json"
            ruta = os.path.join(BASE_DIR, "content", "personajes", nombre_archivo)
        else:
            # Si no hay personajes, crear un personaje por defecto
            return {
                "id": "default",
                "nombre": "Personaje Histórico",
                "descripcion": "Un personaje de la historia local.",
                "frase": "La historia es el testigo de los tiempos, la luz de la verdad.",
                "epoca": "Siglo XX",
                "contexto": "Este es un personaje genérico creado por defecto."
            }
    
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            personaje = json.load(f)
            # Añadir el ID al personaje si no lo tiene
            if "id" not in personaje:
                personaje["id"] = id_personaje or nombre_archivo.replace('.json', '')
            return personaje
    except Exception as e:
        print(f"Error al cargar personaje {nombre_archivo}: {str(e)}")
        return {"error": f"No se pudo cargar el personaje: {str(e)}"}

def cargar_qa_personaje(personaje_id=None):
    """
    Carga preguntas y respuestas predefinidas para un personaje.
    
    Args:
        personaje_id (str, optional): ID del personaje. Default None.
        
    Returns:
        dict: Diccionario de preguntas y respuestas.
    """
    try:
        # Primero intentamos cargar QA específico del personaje
        if personaje_id:
            ruta = os.path.join(BASE_DIR, "content", "qa", f"{personaje_id}_qa.json")
            if os.path.exists(ruta):
                with open(ruta, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # Convertir a diccionario para búsqueda rápida
                    return {item["pregunta"].lower(): item["respuesta"] for item in data}
        
        # Si no hay QA específico, cargamos QA general
        ruta_general = os.path.join(BASE_DIR, "content", "qa", "general_qa.json")
        if os.path.exists(ruta_general):
            with open(ruta_general, "r", encoding="utf-8") as f:
                data = json.load(f)
                return {item["pregunta"].lower(): item["respuesta"] for item in data}
        
        # Si no hay datos, devolvemos un diccionario vacío
        return {}
    except Exception as e:
        print(f"Error al cargar QA: {str(e)}")
        return {}

def cargar_clave_openai():
    """
    Carga la clave de API de OpenAI desde el archivo .env.
    
    Returns:
        str: La clave de API o None si no está configurada.
    """
    load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))
    return os.getenv("OPENAI_API_KEY")

def respuesta_basada_en_keyword(pregunta, personaje_id=None):
    """
    Genera una respuesta básica basada en palabras clave.
    Útil como fallback cuando la API de OpenAI no está disponible.
    
    Args:
        pregunta (str): La pregunta del usuario
        personaje_id (str, optional): ID del personaje
        
    Returns:
        str: Respuesta generada
    """
    pregunta = pregunta.lower()
    personaje = cargar_personaje(personaje_id)
    
    # Intentar encontrar respuesta en el QA predefinido
    qa_dict = cargar_qa_personaje(personaje_id)
    if pregunta in qa_dict:
        return qa_dict[pregunta]
    
    # Buscar la pregunta más similar (aproximación simple)
    for q, r in qa_dict.items():
        if any(keyword in pregunta for keyword in q.split()):
            return r
    
    # Si no hay coincidencias, usar respuestas genéricas basadas en palabras clave
    nombre = personaje.get("nombre", "Personaje histórico")
    
    if "quien" in pregunta or "quién" in pregunta or "eres" in pregunta:
        return f"Soy {nombre}. {personaje.get('descripcion', '')}"
    
    elif "donde" in pregunta or "dónde" in pregunta or "lugar" in pregunta:
        lugar = personaje.get("ubicacion", {}).get("lugar", "varios lugares")
        return f"Mi historia está vinculada principalmente a {lugar}."
    
    elif "cuando" in pregunta or "cuándo" in pregunta or "año" in pregunta or "siglo" in pregunta:
        epoca = personaje.get("epoca", "una época pasada")
        return f"Viví durante {epoca}."
    
    elif "por qué" in pregunta or "porque" in pregunta or "motivo" in pregunta:
        return f"Hay varias razones para ello. {personaje.get('frase', '')}"
    
    # Respuesta por defecto
    return f"Interesante pregunta. Como {nombre}, podría decir que {personaje.get('frase', 'la historia siempre tiene mucho que enseñarnos')}. ¿Hay algo más específico que quieras saber sobre mí?"

# Cambiar el nombre del módulo para que coincida con el archivo existente
# Si utils_mejorado no existe, se debe usar utils en su lugar.