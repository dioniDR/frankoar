#!/bin/bash

# Ir al directorio del backend
cd backend

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
  echo "Creando entorno virtual..."
  python -m venv venv
fi

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Ejecutar servidor
echo "Iniciando servidor en http://localhost:8000"
uvicorn main:app --reload --host 0.0.0.0 --port 8000
