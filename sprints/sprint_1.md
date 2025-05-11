# Sprint 1 - Backend Básico

**Fecha de inicio:** [Fecha actual]  
**Fecha de finalización:** [14 días después de la fecha actual]  
**Duración:** 2 semanas

## Objetivo del Sprint

Implementar la estructura básica del backend con FastAPI, incluyendo endpoints para personajes, historias y el sistema de geolocalización básico. Al final de este sprint, deberíamos tener un servidor funcional que permita obtener información de personajes históricos y buscar personajes cercanos a una ubicación.

## Elementos del Backlog Seleccionados

### 1. Implementar Endpoints Básicos
- **Descripción:** Crear los endpoints core para el MVP
- **Criterios de aceptación:**
  - GET /personajes - lista todos los personajes
  - GET /personaje/{id} - obtiene un personaje específico
  - GET /avatar - obtiene información del avatar
  - GET /historia - obtiene narrativa histórica
  - Documentación Swagger completa
- **Estimación:** 3 días
- **Asignado a:** Yo
- **Estado:** Por hacer

### 2. Mejorar Sistema de Personajes
- **Descripción:** Revisar y mejorar la estructura de datos de personajes
- **Criterios de aceptación:**
  - Esquema JSON consistente
  - Validación de datos requeridos
  - Manejo de errores
  - Al menos 2 personajes completos
- **Estimación:** 2 días
- **Asignado a:** Yo
- **Estado:** Por hacer

### 3. Implementar Sistema Q&A Básico
- **Descripción:** Sistema básico de preguntas y respuestas
- **Criterios de aceptación:**
  - Endpoint POST /preguntar
  - Búsqueda por palabras clave
  - Respuestas predefinidas
  - Fallback para preguntas desconocidas
- **Estimación:** 2 días
- **Asignado a:** Yo
- **Estado:** Por hacer

### 4. Implementar Búsqueda por Geolocalización
- **Descripción:** Sistema para encontrar personajes cercanos a una ubicación
- **Criterios de aceptación:**
  - Endpoint POST /personajes_cercanos
  - Algoritmo de distancia Haversine
  - Ordenamiento por proximidad
  - Filtro por radio de búsqueda
- **Estimación:** 2 días
- **Asignado a:** Yo
- **Estado:** Por hacer

### 5. Añadir Tests Básicos
- **Descripción:** Pruebas básicas para verificar funcionamiento
- **Criterios de aceptación:**
  - Tests para cada endpoint
  - Verificación de carga de personajes
  - Validación de formatos JSON
  - Script de prueba automatizado
- **Estimación:** 1 día
- **Asignado a:** Yo
- **Estado:** Por hacer

## Planificación Diaria

### Semana 1

| Día | Tarea | Horas Estimadas |
|-----|-------|-----------------|
| 1   | Configuración inicial del entorno FastAPI | 2h |
| 1   | Implementar GET /personajes | 2h |
| 2   | Implementar GET /personaje/{id} | 2h |
| 2   | Implementar GET /avatar | 2h |
| 3   | Implementar GET /historia | 2h |
| 3   | Documentación Swagger | 2h |
| 4   | Revisión estructura JSON personajes | 3h |
| 4   | Implementar validación de datos | 1h |
| 5   | Crear 2 personajes completos | 4h |

### Semana 2

| Día | Tarea | Horas Estimadas |
|-----|-------|-----------------|
| 6   | Implementar POST /preguntar | 4h |
| 7   | Sistema de palabras clave y fallback | 4h |
| 8   | Algoritmo Haversine | 2h |
| 8   | Implementar POST /personajes_cercanos | 2h |
| 9   | Optimización búsqueda geoespacial | 4h |
| 10  | Escribir tests para endpoints | 4h |
| 10  | Scripts de prueba automatizados | 2h |

## Daily Scrums

### Día 1 - [Fecha]
- **Completado:** [Llenar durante el sprint]
- **Por hacer hoy:** [Llenar durante el sprint]
- **Impedimentos:** [Llenar durante el sprint]

### Día 2 - [Fecha]
- **Completado:** [Llenar durante el sprint]
- **Por hacer hoy:** [Llenar durante el sprint]
- **Impedimentos:** [Llenar durante el sprint]

[Continuar para los demás días...]

## Revisión del Sprint

[Completar al finalizar el sprint]

### Elementos Completados
- [Listar elementos completados con éxito]

### Elementos No Completados
- [Listar elementos no completados y razones]

### Demostración
- [Notas sobre la demostración del incremento]

## Retrospectiva

[Completar al finalizar el sprint]

### Lo que funcionó bien
- [Listar aspectos positivos]

### Lo que podría mejorar
- [Listar áreas de mejora]

### Acciones para el próximo Sprint
- [Listar acciones concretas para el Sprint 2]
