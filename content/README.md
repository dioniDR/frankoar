# Contenido para FRANKO.AR

Esta carpeta contiene los archivos de datos para los personajes históricos del sistema FRANKO.AR.

## Estructura de carpetas

```
content/
├── personajes/  - Archivos JSON con información de los personajes
│   ├── frida_kahlo.json
│   └── george_washington.json
├── qa/          - Archivos JSON con preguntas y respuestas predefinidas
│   ├── frida_kahlo_qa.json
│   └── george_washington_qa.json
└── README.md    - Este archivo
```

## Guía rápida para añadir personajes

1. **Crear archivo del personaje**: 
   - Nombre: `[id_personaje].json`
   - Ubicación: `content/personajes/`
   - Contenido: Información completa del personaje

2. **Crear archivo de preguntas y respuestas**:
   - Nombre: `[id_personaje]_qa.json`
   - Ubicación: `content/qa/`
   - Contenido: Lista de preguntas y respuestas predefinidas

3. **Añadir imagen del personaje**:
   - Nombre: `[id_personaje].png`
   - Ubicación: `static/avatares/`
   - Formato: PNG con fondo transparente

## Estructura de un archivo de personaje

```json
{
  "id": "nombre_unico",
  "nombre": "Nombre Completo",
  "descripcion": "Descripción del personaje",
  "frase": "Frase característica",
  "epoca": "Época histórica",
  "contexto": "Contexto histórico",
  "ubicacion": {
    "lat": 0.0000,
    "lng": 0.0000,
    "lugar": "Nombre del lugar"
  }
}
```

## Estructura de un archivo de preguntas y respuestas

```json
[
  {
    "pregunta": "¿Pregunta 1?",
    "respuesta": "Respuesta 1"
  },
  {
    "pregunta": "¿Pregunta 2?",
    "respuesta": "Respuesta 2"
  }
]
```

## Guía completa de implementación

Para instrucciones detalladas sobre cómo implementar personajes correctamente, incluyendo mejores prácticas y ejemplos, consulta la guía completa en:

`/docs/guias/implementacion_personajes.md`

Esta guía contiene información sobre:
- Cómo estructurar correctamente los archivos JSON
- Recomendaciones para escribir en primera persona
- Cómo añadir ubicaciones geográficas múltiples
- Formatos recomendados para imágenes
- Proceso de prueba para verificar que el personaje funcione correctamente

## Soporte

Si tienes dudas sobre la implementación de personajes, consulta la documentación o contacta al equipo de desarrollo.