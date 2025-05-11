# Product Backlog FRANKO.AR

## Épicas

### 1. Backend Básico
- [ ] **Estructura FastAPI**
  - [x] Configuración inicial
  - [ ] Endpoints básicos
  - [x] Estructura de carpetas
  - [ ] Documentación Swagger
- [ ] **Sistema de Personajes**
  - [x] Carga desde JSON
  - [ ] Estructura de datos completa
  - [ ] Validación de esquema
  - [ ] Documentación de formato
- [ ] **Sistema Q&A Básico**
  - [x] Respuestas predefinidas
  - [ ] Sistema fallback
  - [ ] Tests automáticos
  - [ ] Documentación de formato Q&A
- [ ] **Integración OpenAI**
  - [ ] Conexión básica
  - [ ] Manejo de errores
  - [ ] Control de costos/límites
  - [ ] Fallback sin conexión
- [ ] **Geolocalización**
  - [ ] Algoritmo de distancia
  - [ ] Búsqueda de personajes cercanos
  - [ ] Optimización para muchos personajes
  - [ ] Tests de precisión

### 2. Frontend Básico
- [ ] **Interfaz Mínima**
  - [ ] HTML/CSS estructura
  - [ ] Visualización avatar
  - [ ] Responsive design
  - [ ] Tema visual coherente
- [ ] **Conexión a API**
  - [ ] Fetch básico
  - [ ] Manejo de errores
  - [ ] Indicadores de carga
  - [ ] Caché local
- [ ] **Geolocalización Cliente**
  - [ ] Solicitud de permisos
  - [ ] Obtención de coordenadas
  - [ ] Envío al backend
  - [ ] Manejo de errores GPS
- [ ] **Interacción con Personaje**
  - [ ] Formulario de preguntas
  - [ ] Historial de conversación
  - [ ] Animaciones básicas
  - [ ] Feedback visual

### 3. Realidad Aumentada
- [ ] **Estructura AR.js/A-Frame**
  - [ ] Configuración básica
  - [ ] Integración con la web
  - [ ] Permisos de cámara
  - [ ] Compatibilidad navegadores
- [ ] **Avatar Básico**
  - [ ] Mostrar imagen 2D
  - [ ] Escala apropiada
  - [ ] Orientación hacia usuario
  - [ ] Tests en dispositivos varios
- [ ] **Anclaje GPS**
  - [ ] Posicionamiento por coordenadas
  - [ ] Ajuste de altura
  - [ ] Manejo de errores GPS
  - [ ] Optimización de precisión
- [ ] **Interacción AR**
  - [ ] Mostrar diálogo
  - [ ] Mostrar botones AR
  - [ ] Gestos básicos
  - [ ] Feedback de interacción

### 4. Contenido
- [ ] **Estructura de Datos**
  - [x] Formato personajes
  - [x] Formato Q&A
  - [ ] Esquema validación
  - [ ] Documentación detallada
- [ ] **Personajes MVP**
  - [x] George Washington
  - [x] Francisco Miranda
  - [ ] Personaje local
  - [ ] Tests de calidad contenido
- [ ] **Contenido Q&A**
  - [ ] 10+ preguntas por personaje
  - [ ] Categorización de preguntas
  - [ ] Keywords para búsqueda
  - [ ] Validación cultural/histórica
- [ ] **Assets Visuales**
  - [ ] Avatares por personaje
  - [ ] Iconos de interfaz
  - [ ] Recursos AR
  - [ ] Optimización para móvil

## Sprint 1: Backend Básico

### Objetivo
Implementar la estructura básica del backend con FastAPI, incluyendo endpoints para personajes y geolocalización.

### Elementos del Backlog Seleccionados

1. **Implementar Endpoints Básicos**
   - Descripción: Crear los endpoints core para el MVP
   - Criterios de aceptación:
     - GET /personajes - lista todos los personajes
     - GET /personaje/{id} - obtiene un personaje específico
     - POST /personajes_cercanos - busca por coordenadas
     - Documentación Swagger completa
   - Estimación: 3 días
   - Prioridad: Alta

2. **Mejorar Sistema de Personajes**
   - Descripción: Revisar y mejorar la estructura de datos de personajes
   - Criterios de aceptación:
     - Esquema JSON consistente
     - Validación de datos requeridos
     - Manejo de errores
     - Al menos 2 personajes completos
   - Estimación: 2 días
   - Prioridad: Alta

3. **Implementar Sistema Q&A Básico**
   - Descripción: Sistema básico de preguntas y respuestas
   - Criterios de aceptación:
     - Endpoint POST /preguntar
     - Búsqueda por palabras clave
     - Respuestas predefinidas
     - Fallback para preguntas desconocidas
   - Estimación: 2 días
   - Prioridad: Media

4. **Implementar Búsqueda por Geolocalización**
   - Descripción: Sistema para encontrar personajes cercanos a una ubicación
   - Criterios de aceptación:
     - Algoritmo de distancia Haversine
     - Ordenamiento por proximidad
     - Filtro por radio de búsqueda
     - Rendimiento con muchos personajes
   - Estimación: 2 días
   - Prioridad: Media

5. **Añadir Tests Básicos**
   - Descripción: Pruebas básicas para verificar funcionamiento
   - Criterios de aceptación:
     - Tests para cada endpoint
     - Verificación de carga de personajes
     - Validación de formatos JSON
     - Script de prueba automatizado
   - Estimación: 1 día
   - Prioridad: Baja

## Sprint 2: Frontend y Conexión

### Objetivo
Implementar la interfaz básica y conectarla al backend.

### Elementos del Backlog (Preliminar)

1. **Implementar Interfaz HTML/CSS/JS**
   - Descripción: Crear la estructura visual básica
   - Criterios de aceptación: [Por definir al iniciar Sprint 2]
   - Estimación: 3 días
   - Prioridad: Alta

2. **Implementar Conexión a API**
   - Descripción: Conectar frontend con backend
   - Criterios de aceptación: [Por definir al iniciar Sprint 2]
   - Estimación: 2 días
   - Prioridad: Alta

3. **Implementar Geolocalización Cliente**
   - Descripción: Solicitar y usar ubicación del usuario
   - Criterios de aceptación: [Por definir al iniciar Sprint 2]
   - Estimación: 2 días
   - Prioridad: Media

4. **Implementar Interacción con Personaje**
   - Descripción: Sistema de preguntas y respuestas en frontend
   - Criterios de aceptación: [Por definir al iniciar Sprint 2]
   - Estimación: 3 días
   - Prioridad: Media
