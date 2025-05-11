# Documentación de Endpoints API - FRANKO.AR

Esta documentación detalla todos los endpoints disponibles en la API de FRANKO.AR, su funcionamiento, parámetros y ejemplos de uso.

## Endpoints Principales

### 1. Listado de Personajes

**Endpoint:** `GET /personajes`

**Descripción:** Obtiene una lista de todos los personajes históricos disponibles en el sistema.

**Parámetros:** Ninguno

**Respuesta:**
```json
[
  {
    "id": "george_washington",
    "nombre": "George Washington",
    "frase": "La libertad, cuando comienza a echar raíces, es una planta de rápido crecimiento.",
    "epoca": "Siglo XVIII"
  },
  {
    "id": "francisco_miranda",
    "nombre": "Francisco Miranda",
    "frase": "¡Colombianos! Ha sonado la hora de nuestra libertad.",
    "epoca": "Siglo XIX"
  }
]
```

**Uso de ejemplo:**
```javascript
fetch('http://localhost:8000/personajes')
  .then(response => response.json())
  .then(data => console.log(data));
```

---

### 2. Detalle de Personaje

**Endpoint:** `GET /personaje/{id}`

**Descripción:** Obtiene información detallada de un personaje específico.

**Parámetros:**
- `id` (path): Identificador único del personaje

**Respuesta:**
```json
{
  "id": "george_washington",
  "nombre": "George Washington",
  "descripcion": "Militar, estadista y primer presidente de los Estados Unidos...",
  "frase": "La libertad, cuando comienza a echar raíces, es una planta de rápido crecimiento.",
  "epoca": "Siglo XVIII",
  "contexto": "Fui comandante en jefe del Ejército Continental durante la Guerra de Independencia...",
  "ubicacion": {
    "lat": 38.8977,
    "lng": -77.0365,
    "lugar": "Washington D.C., Estados Unidos"
  },
  "datos_adicionales": {
    "nacimiento": "1732",
    "fallecimiento": "1799",
    "logros": ["Victoria en la Guerra de Independencia", "Primer presidente de EE.UU."],
    "reconocimientos": ["Padre de la Patria", "Fundador de la nación estadounidense"]
  },
  "lugares_relacionados": [
    {
      "nombre": "Mount Vernon",
      "lat": 38.7080,
      "lng": -77.0866,
      "descripcion": "Mi hogar y plantación en Virginia..."
    }
  ]
}
```

**Uso de ejemplo:**
```javascript
fetch('http://localhost:8000/personaje/george_washington')
  .then(response => response.json())
  .then(data => console.log(data));
```

---

### 3. Información del Avatar

**Endpoint:** `GET /avatar`

**Descripción:** Obtiene la información básica para presentar el avatar en la interfaz.

**Parámetros:**
- `personaje_id` (query, opcional): ID del personaje. Si no se proporciona, se usa un personaje por defecto.

**Respuesta:**
```json
{
  "id": "george_washington",
  "nombre": "George Washington",
  "frase": "La libertad, cuando comienza a echar raíces, es una planta de rápido crecimiento.",
  "imagen": "/static/avatares/george_washington.png",
  "ubicacion": {
    "lat": 38.8977,
    "lng": -77.0365,
    "lugar": "Washington D.C., Estados Unidos"
  }
}
```

**Uso de ejemplo:**
```javascript
fetch('http://localhost:8000/avatar?personaje_id=george_washington')
  .then(response => response.json())
  .then(data => console.log(data));
```

---

### 4. Historia del Lugar

**Endpoint:** `GET /historia`

**Descripción:** Obtiene la narrativa histórica asociada a un lugar.

**Parámetros:**
- `lugar` (query, opcional): Nombre del lugar. Si no se proporciona, se usa una ubicación por defecto.

**Respuesta:**
```json
{
  "titulo": "El inicio de una revolución",
  "contenido": "En esta plaza nació el espíritu revolucionario de América del Sur...",
  "año": "1810",
  "lugar": "Plaza de Mayo"
}
```

**Uso de ejemplo:**
```javascript
fetch('http://localhost:8000/historia?lugar=Plaza%20de%20Mayo')
  .then(response => response.json())
  .then(data => console.log(data));
```

---

### 5. Preguntar al Personaje (Básico)

**Endpoint:** `POST /preguntar`

**Descripción:** Envía una pregunta al personaje y recibe una respuesta básica.

**Parámetros (JSON):**
```json
{
  "pregunta": "¿Quién eres?",
  "personaje_id": "george_washington"
}
```

**Respuesta:**
```json
{
  "pregunta": "¿Quién eres?",
  "respuesta": "Soy George Washington, primer presidente de los Estados Unidos y comandante del Ejército Continental durante la Guerra de Independencia.",
  "personaje": "George Washington"
}
```

**Uso de ejemplo:**
```javascript
fetch('http://localhost:8000/preguntar', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    pregunta: "¿Quién eres?",
    personaje_id: "george_washington"
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

---

### 6. Consultar con IA (OpenAI)

**Endpoint:** `POST /consultar`

**Descripción:** Envía una pregunta al personaje y recibe una respuesta generada por IA.

**Parámetros (JSON):**
```json
{
  "pregunta": "¿Cómo era la vida en tu época?",
  "personaje_id": "george_washington"
}
```

**Respuesta:**
```json
{
  "personaje": "George Washington",
  "respuesta": "La vida en mi época, el siglo XVIII, era muy diferente a la actual. La mayoría de las personas vivían en áreas rurales y se dedicaban a la agricultura. Las ciudades eran pequeñ