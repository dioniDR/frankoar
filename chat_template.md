# Plantilla para Contexto entre Chats - FRANKO.AR

```
PROYECTO: FRANKO.AR
MÓDULO: [Backend/Frontend/AR/Contenido]
FECHA: [Fecha actual]

ESTADO ACTUAL:
- [Lista de componentes implementados]
- [Estado actual del módulo]
- [Últimos cambios realizados]

ARCHIVOS RELEVANTES:
- [Lista de archivos principales del módulo]
- [Rutas relativas a la raíz del proyecto]

OBJETIVO DE ESTA SESIÓN:
[Descripción clara del objetivo para esta sesión de chat]

LIMITACIONES/REQUISITOS:
- [Restricciones técnicas]
- [Dependencias pendientes]
- [Consideraciones especiales]

CONTEXTO TÉCNICO:
```python
# Ejemplo de código actual relevante
def funcion_actual():
    # Implementación actual
    pass
```

¿Puedes ayudarme a [objetivo específico de esta consulta]?
```

## Ejemplos de Uso

### Ejemplo para Sesión de Backend

```
PROYECTO: FRANKO.AR
MÓDULO: Backend
FECHA: 2025-05-11

ESTADO ACTUAL:
- Endpoints básicos implementados (/personajes, /personaje/{id})
- Sistema de carga de personajes desde JSON funcionando
- Pendiente: Implementación de geolocalización

ARCHIVOS RELEVANTES:
- mvp/backend/main.py - Servidor FastAPI
- mvp/backend/utils.py - Funciones auxiliares
- mvp/backend/content/personajes/*.json - Datos de personajes

OBJETIVO DE ESTA SESIÓN:
Implementar el endpoint POST /personajes_cercanos para buscar personajes históricos cercanos a una ubicación geográfica.

LIMITACIONES/REQUISITOS:
- Debe ser eficiente incluso con muchos personajes
- Debe funcionar con coordenadas GPS (lat, lng)
- Debe permitir filtrar por radio de búsqueda

CONTEXTO TÉCNICO:
```python
# Función actual en utils.py (incompleta)
def distancia_haversine(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia entre dos puntos geográficos usando la fórmula de Haversine.
    """
    # Implementación pendiente
    pass

# Endpoint a implementar en main.py
@app.post("/personajes_cercanos")
async def get_personajes_cercanos(coordenadas: CoordenadaConsulta):
    """
    Encuentra personajes cercanos a una ubicación.
    """
    # Implementación pendiente
    pass
```

¿Puedes ayudarme a implementar correctamente la función distancia_haversine y el endpoint /personajes_cercanos?
```

### Ejemplo para Sesión de Frontend

```
PROYECTO: FRANKO.AR
MÓDULO: Frontend
FECHA: 2025-05-13

ESTADO ACTUAL:
- Estructura HTML/CSS básica implementada
- Visualización de avatar funcionando
- Pendiente: Implementación de geolocalización cliente

ARCHIVOS RELEVANTES:
- mvp/frontend/index.html - Página principal
- mvp/frontend/main.js - Lógica JavaScript
- mvp/frontend/style.css - Estilos

OBJETIVO DE ESTA SESIÓN:
Implementar la funcionalidad para obtener la ubicación del usuario y mostrar personajes cercanos.

LIMITACIONES/REQUISITOS:
- Debe solicitar permisos de geolocalización al usuario
- Debe manejar errores de permisos denegados
- Debe mostrar indicador mientras busca personajes

CONTEXTO TÉCNICO:
```javascript
// Fragmento actual de main.js
document.getElementById("btn-historia").addEventListener("click", () => {
  fetch("http://localhost:8000/historia")
    .then(response => response.json())
    .then(data => {
      document.getElementById("historia").innerText = data.titulo + "\n\n" + data.contenido;
    })
    .catch(err => {
      document.getElementById("historia").innerText = "Error al obtener historia.";
    });
});

// Función a implementar
function obtenerUbicacion() {
  // Implementación pendiente
}
```

¿Puedes ayudarme a implementar la función obtenerUbicacion() y la lógica para mostrar personajes cercanos?
```

### Ejemplo para Sesión de AR

```
PROYECTO: FRANKO.AR
MÓDULO: AR
FECHA: 2025-05-15

ESTADO ACTUAL:
- Estructura de carpeta mvp/ar/ creada
- Pendiente: Implementación básica de AR.js/A-Frame

ARCHIVOS RELEVANTES:
- mvp/ar/index.html - Página AR (por crear)

OBJETIVO DE ESTA SESIÓN:
Crear una implementación básica de AR.js y A-Frame que muestre un avatar 2D en coordenadas GPS.

LIMITACIONES/REQUISITOS:
- Debe funcionar en navegadores móviles
- Debe mostrar avatar anclado a coordenadas GPS
- Debe conectarse al backend para obtener datos del personaje

CONTEXTO TÉCNICO:
No hay código existente en este módulo aún.

¿Puedes ayudarme a crear la estructura básica de AR.js/A-Frame para mostrar un avatar 2D anclado a coordenadas GPS?
```

## Instrucciones de Uso

1. Copia la plantilla al inicio de cada nueva sesión de chat con Claude o ChatGPT.
2. Completa todas las secciones con información relevante sobre el estado actual del proyecto.
3. Incluye solo el código relevante para la consulta actual, evitando compartir todo el código.
4. Sé específico sobre lo que necesitas, proporcionando contexto suficiente.
5. Actualiza esta plantilla según evolucione el proyecto.