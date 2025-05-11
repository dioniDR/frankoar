from openai import OpenAI
from utils_mejorado import cargar_clave_openai, cargar_qa_personaje, respuesta_basada_en_keyword

def responder_con_openai(pregunta: str, personaje: dict) -> dict:
    """
    Genera una respuesta personalizada usando OpenAI API basada en el personaje.
    
    Args:
        pregunta (str): Pregunta del usuario
        personaje (dict): Datos del personaje histórico
        
    Returns:
        dict: Respuesta generada con información del personaje
    """
    # Obtener información del personaje
    personaje_id = personaje.get("id", "default")
    nombre = personaje.get("nombre", "Personaje histórico")
    descripcion = personaje.get("descripcion", "Sin descripción.")
    frase = personaje.get("frase", "")
    contexto = personaje.get("contexto", "")
    epoca = personaje.get("epoca", "")
    
    # Intentar encontrar respuesta en QA predefinido
    qa_dict = cargar_qa_personaje(personaje_id)
    pregunta_lower = pregunta.lower()
    
    # Verificar si hay una respuesta predefinida exacta
    if pregunta_lower in qa_dict:
        return {
            "personaje": nombre,
            "respuesta": qa_dict[pregunta_lower],
            "fuente": "qa_predefinido"
        }
    
    # Construir el prompt con contexto enriquecido
    prompt = f"""Actúa como {nombre}, un personaje histórico que habla en primera persona con visitantes.

INFORMACIÓN SOBRE MÍ:
- Nombre: {nombre}
- Época: {epoca}
- Descripción: {descripcion}
- Contexto histórico: {contexto}
- Frase característica: "{frase}"

INSTRUCCIONES:
1. Responde SIEMPRE en primera persona, como si fueras {nombre} hablando directamente con un visitante.
2. Mantén un tono conversacional y amigable, pero coherente con tu época y personalidad.
3. Menciona detalles históricos precisos cuando sea relevante.
4. Si no conoces la respuesta a algo específico sobre tu vida, puedes decir algo como "Ese detalle no quedó registrado en mis memorias" en lugar de inventar.
5. Limita tu respuesta a 3-4 oraciones máximo para mantener la conversación fluida.

Pregunta del visitante: {pregunta}"""

    print("\n--- PROMPT GENERADO ---\n" + prompt + "\n------------------------")

    # Obtener la clave de API
    api_key = cargar_clave_openai()
    
    # Si no hay clave API, usar respuesta basada en keywords como fallback
    if not api_key:
        respuesta = respuesta_basada_en_keyword(pregunta, personaje_id)
        return {
            "personaje": nombre,
            "respuesta": respuesta,
            "fuente": "fallback_keywords"
        }

    try:
        # Configurar cliente de OpenAI
        client = OpenAI(api_key=api_key)
        
        # Llamar a la API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un personaje histórico que habla con visitantes en un espacio público."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        
        # Extraer respuesta
        texto = response.choices[0].message.content.strip()
        return {
            "personaje": nombre,
            "respuesta": texto,
            "fuente": "openai"
        }
    except Exception as e:
        # En caso de error, usar el sistema de fallback
        respuesta = respuesta_basada_en_keyword(pregunta, personaje_id)
        return {
            "personaje": nombre,
            "respuesta": respuesta,
            "fuente": "fallback_error",
            "error": str(e)
        }