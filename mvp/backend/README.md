# API Mínima - FRANKO.AR

Este módulo permite probar el MVP del backend educativo con FastAPI.

## 🚀 Cómo ejecutar

```bash
# 1. Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar el servidor
uvicorn main:app --reload
```

## Rutas disponibles

- `GET /avatar` → Información básica del avatar
- `GET /historia` → Historia breve del lugar
- `POST /preguntar` → Simula una respuesta de IA

## 📁 Recursos estáticos

Agrega imágenes a la carpeta `static/`. Por ejemplo, `static/avatar.png`
