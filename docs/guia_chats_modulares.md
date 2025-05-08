# Guía de chats modulares - FRANKO.AR

En FRANKO.AR, cada módulo técnico funciona como un "chat especializado". Esta estructura permite dividir el proyecto en partes pequeñas, comprensibles y reutilizables.

## ¿Qué es un chat modular?
Un chat modular es un entorno de desarrollo orientado a una sola tarea. Cada uno recuerda su contexto, estructura interna y limitaciones del MVP.

## Módulos del MVP

| Módulo              | Descripción                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| 📍 Anclaje Geográfico | Fija la experiencia a un punto físico (coordenadas o referencia manual).     |
| 🧍 Avatar             | Muestra un personaje histórico en AR, anclado a una ubicación específica.   |
| 🧾 Narrativa          | Presenta la historia asociada al personaje, breve y contextual.             |
| 🤖 IA                | Permite una interacción limitada con el avatar mediante lenguaje natural.   |
| 📝 Documentación      | Organiza la comunicación, documentación y entregas.                         |

## Extensiones (futuras)

- Realidad mixta avanzada
- Interacción con gestos o voz
- Integración con bases de datos públicas

Estas se documentan en `/docs/extensiones.md`, pero no forman parte del MVP.

## Ventajas del enfoque modular

- Aísla problemas técnicos
- Facilita pruebas por separado
- Mejora la colaboración entre equipos
- Permite escalar sin romper lo que ya funciona

Cada chat puede ser documentado, entregado y validado por separado, haciendo que el desarrollo sea más claro y sostenible.
