# Notas de Interés - FRANKO.AR

Este documento recopila temas recurrentes, aplicaciones, repositorios y conceptos clave discutidos durante el desarrollo del proyecto FRANKO.AR. Sirve como referencia rápida para conceptos importantes y recursos recomendados.

## Temas Recurrentes

### Énfasis en Estructura Modular
- **Enfoque de componentes independientes**: Backend, Frontend, AR
- **Desarrollo por módulos**: Permite avanzar en paralelo y tener entregables concretos
- **Arquitectura flexible**: Facilita escalabilidad y mantenimiento futuro
- **Comunicación clara entre módulos**: APIs bien definidas

### Metodología Scrum Adaptada
- **Sprints cortos**: 1-2 semanas para mantener el impulso
- **Product Backlog priorizado**: Enfoque en MVP primero
- **Daily Scrums**: Seguimiento diario del progreso
- **Revisiones y retrospectivas**: Mejora continua del proceso

### Enfoque en Geolocalización
- **Anclaje geográfico preciso**: Es un diferenciador clave del proyecto
- **Algoritmo Haversine**: Para cálculo de distancias geográficas
- **Precisión vs performance**: Balance para muchos personajes
- **Experiencia en lugares reales**: Valor principal para usuarios

### Asistencia con IA
- **Uso eficiente de tokens**: Minimizar costos con prompts específicos
- **Continuidad contextual**: Estructura clara entre chats
- **Equilibrio código/documentación**: No generar código innecesariamente
- **Chat especializado por módulo**: Mejor contexto y enfoque

## Aplicaciones Recomendadas

### Realidad Aumentada
- **AR.js**: Framework para AR web (https://github.com/AR-js-org/AR.js)
- **A-Frame**: Creación de experiencias VR/AR web (https://aframe.io/)
- **AR.js Studio**: Editor visual para AR web (https://ar-js-org.github.io/studio/)
- **TimeLooper**: Experiencias históricas geolocalizadas (referencia comercial)

### Desarrollo Backend
- **FastAPI**: Framework para APIs en Python (https://fastapi.tiangolo.com/)
- **Swagger UI**: Documentación interactiva de API (integrada en FastAPI)
- **Pydantic**: Validación de datos en Python (usado por FastAPI)
- **Uvicorn**: Servidor ASGI para Python (para ejecutar FastAPI)

### Geolocalización
- **Turf.js**: Análisis geoespacial en JavaScript (https://turfjs.org/)
- **Leaflet**: Librería para mapas interactivos (https://leafletjs.com/)
- **OpenLayers**: Alternativa a Leaflet para mapas (https://openlayers.org/)
- **Nominatim**: Servicio de geocodificación (https://nominatim.org/)

### Gestión de Proyectos
- **Sprint planning poker**: Estimación de tareas (técnica)
- **Burndown charts**: Visualización de progreso del sprint
- **Daily standups**: Formato para reuniones diarias (15 min)
- **User story mapping**: Técnica de organización de historias de usuario

## Repositorios de Referencia

### AR Geolocalizada
- **AR.js Location Based**: https://github.com/AR-js-org/AR.js/tree/master/aframe/examples/location-based
- **HistoryInAR**: https://github.com/simon-tiger/history-in-ar
- **Wikitude Open Source Examples**: https://github.com/Wikitude/wikitude-sdk-samples
- **Dynamic AR Depth Mapping**: https://github.com/google-ar/arcore-depth-lab

### Proyectos Similares
- **Open History Map**: https://github.com/OpenHistoricalMap
- **Field Day**: https://github.com/fieldday-ai
- **Arches**: https://github.com/archesproject/arches
- **OpenHistoricalMap**: https://github.com/OpenHistoricalMap

### Componentes Específicos
- **A-Frame GPS**: https://github.com/aframe-ar/aframe-ar
- **Character Director for A-Frame**: https://github.com/wiserim/cyberbrain
- **Memory Context Preservation**: https://github.com/kkimdev/pytorch-compiled-memories
- **Web Speech y Speech Recognition**: https://github.com/mdn/dom-examples/tree/main/web-speech-api

## Conceptos Clave Técnicos

### Arquitectura Backend
- **Endpoints RESTful**: Estructura clara de recursos
- **Manejo de errores HTTP**: Códigos de estado apropiados
- **Asincronía en FastAPI**: Uso de async/await
- **Validación de parámetros**: Tipado fuerte con Pydantic

### AR Web Concepts
- **Marker-based AR**: Usando marcadores físicos
- **Location-based AR**: Usando coordenadas GPS
- **SLAM (Simultaneous Localization and Mapping)**: Para AR más avanzada
- **Occlusion**: Para que objetos virtuales interactúen con reales

### Integración IA
- **Prompting efectivo**: Estructurar instrucciones claras
- **Fallback system**: Respuestas predefinidas cuando falla IA
- **Sistema de keywords**: Implementación simple para respuestas
- **Contexto histórico preciso**: Asegurar respuestas fidedignas

### Performance Considerations
- **Optimización de consultas geoespaciales**: Algoritmos eficientes
- **Assets ligeros para AR**: Modelos 3D/2D optimizados
- **Caching de respuestas**: Para preguntas frecuentes
- **Lazy loading**: Cargar contenido según proximidad

## Sugerencias Recurrentes

### Enfoque "MVP First"
- **Funcional sobre perfecto**: Priorizar que funcione
- **Iteraciones rápidas**: Implementar, probar, ajustar
- **Testing en dispositivos reales**: No confiar solo en emuladores
- **Feedback temprano**: Probar con usuarios reales lo antes posible

### Estructuración del Código
- **Modularidad**: Separación clara de responsabilidades
- **Documentación inline**: Comentarios explicativos clave
- **Tests unitarios**: Para componentes críticos
- **CI/CD simple**: Automatización básica de pruebas y despliegue

### UX/UI Considerations
- **Progressive disclosure**: No abrumar al usuario
- **Feedback visual**: Indicadores de carga y progreso
- **Adaptación móvil**: Diseño responsive prioritario
- **Permisos explícitos**: Solicitar geolocalización claramente

## Documentos de Referencia

- **estructura_proyecto.md**: Definición de carpetas y archivos
- **endpoints.md**: Documentación completa de la API
- **backlog.md**: Lista priorizada de funcionalidades
- **estado_frankoar.py**: Script para verificar estado del proyecto
- **generar_prompt.py**: Script para generar prompts de chat
- **sprint_1.md**: Definición y seguimiento del primer sprint

## Próximos Temas a Explorar

- Implementación específica de AR.js con anclaje GPS
- Optimización de geolocalización para entornos urbanos
- Estrategias de caching para contenido histórico
- Técnicas avanzadas de integración con OpenAI API
- Estrategias de prueba para AR en diferentes dispositivos
