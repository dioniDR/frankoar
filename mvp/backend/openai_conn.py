from openai import OpenAI
from utils import cargar_clave_openai

api_key = cargar_clave_openai()
client = OpenAI(api_key=api_key)

def responder_con_openai(pregunta: str, personaje: dict) -> dict:
    nombre = personaje.get("nombre", "Personaje")
    descripcion = personaje.get("descripcion", "Sin descripción.")
    frase = personaje.get("frase", "")

    prompt = f"""Actúa como {nombre}. Eres un personaje histórico de América Latina.
Descripción: {descripcion}
Frase: \"{frase}\"  
Usuario: {pregunta}"""

    print("\n--- PROMPT GENERADO ---\n" + prompt + "\n------------------------")

    if not api_key:
        return {
            "personaje": nombre,
            "respuesta": "(Simulación) No se encontró la clave OPENAI_API_KEY. Aquí respondería el personaje."
        }

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Responde en primera persona como un personaje histórico que habla con visitantes en una plaza."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.7,
        )
        texto = response.choices[0].message.content.strip()
        return {"personaje": nombre, "respuesta": texto}
    except Exception as e:
        return {
            "personaje": nombre,
            "respuesta": f"(Simulación por error) {str(e)}"
        }
