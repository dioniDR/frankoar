#!/usr/bin/env python3
# estado_frankoar.py - Script para verificar el estado del proyecto FRANKO.AR

import os
import json
import sys
from pathlib import Path
import requests
from datetime import datetime

# Colores para la terminal
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def print_header(text):
    """Imprime un encabezado con formato"""
    print(f"\n{Colors.BLUE}{Colors.BOLD}{text}{Colors.ENDC}")

def print_status(description, status, details=""):
    """Imprime el estado de un componente con formato de color"""
    if status == "OK":
        icon = "✅"
        color = Colors.GREEN
    elif status == "PARTIAL":
        icon = "⚠️"
        color = Colors.YELLOW
    elif status == "MISSING":
        icon = "❌"
        color = Colors.RED
    else:
        icon = "ℹ️"
        color = Colors.BLUE
    
    print(f"{color}{icon} {description}{Colors.ENDC}")
    if details:
        print(f"   {details}")

def check_file_exists(filepath):
    """Verifica si un archivo existe"""
    return Path(filepath).is_file()

def check_dir_exists(dirpath):
    """Verifica si un directorio existe"""
    return Path(dirpath).is_dir()

def check_server_running():
    """Verifica si el servidor FastAPI está en ejecución"""
    try:
        response = requests.get("http://localhost:8000/", timeout=1)
        return True
    except:
        return False

def count_files(directory, extension):
    """Cuenta archivos con una extensión específica en un directorio"""
    if not os.path.exists(directory):
        return 0
    return len([f for f in os.listdir(directory) if f.endswith(extension)])

def main():
    """Función principal para verificar el estado del proyecto"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"{Colors.BOLD}ESTADO DEL PROYECTO FRANKO.AR - {now}{Colors.ENDC}")
    
    # Verificar estructura principal
    print_header("ESTRUCTURA DE CARPETAS")
    
    project_root = os.getcwd()
    mvp_dir = os.path.join(project_root, "mvp")
    docs_dir = os.path.join(project_root, "docs")
    
    if check_dir_exists(mvp_dir):
        print_status("Carpeta MVP", "OK")
    else:
        print_status("Carpeta MVP", "MISSING", "Crea la carpeta principal: mkdir -p mvp")
        os.makedirs(mvp_dir, exist_ok=True)
    
    if check_dir_exists(docs_dir):
        print_status("Carpeta docs", "OK")
    else:
        print_status("Carpeta docs", "MISSING", "Crea la carpeta de documentación: mkdir -p docs")
        os.makedirs(docs_dir, exist_ok=True)
    
    # Verificar Backend
    print_header("BACKEND")
    
    backend_dir = os.path.join(mvp_dir, "backend")
    if check_dir_exists(backend_dir):
        print_status("Carpeta backend", "OK")
        
        # Verificar archivos principales
        if check_file_exists(os.path.join(backend_dir, "main.py")):
            print_status("main.py", "OK")
        else:
            print_status("main.py", "MISSING", "Archivo principal del servidor no encontrado")
        
        if check_file_exists(os.path.join(backend_dir, "utils.py")):
            print_status("utils.py", "OK")
        else:
            print_status("utils.py", "MISSING", "Funciones de utilidad no encontradas")
        
        if check_file_exists(os.path.join(backend_dir, "openai_conn.py")):
            print_status("openai_conn.py", "OK")
        else:
            print_status("openai_conn.py", "MISSING", "Conexión con OpenAI no implementada")
        
        # Verificar contenido
        content_dir = os.path.join(backend_dir, "content")
        personajes_dir = os.path.join(content_dir, "personajes")
        qa_dir = os.path.join(content_dir, "qa")
        
        if check_dir_exists(content_dir):
            print_status("Carpeta content", "OK")
            
            if check_dir_exists(personajes_dir):
                personajes_count = count_files(personajes_dir, ".json")
                if personajes_count > 0:
                    print_status(f"Personajes: {personajes_count}", "OK")
                else:
                    print_status("Personajes", "MISSING", "No hay archivos JSON de personajes")
            else:
                print_status("Carpeta personajes", "MISSING", "Crea: mkdir -p mvp/backend/content/personajes")
                os.makedirs(personajes_dir, exist_ok=True)
            
            if check_dir_exists(qa_dir):
                qa_count = count_files(qa_dir, ".json")
                if qa_count > 0:
                    print_status(f"Archivos Q&A: {qa_count}", "OK")
                else:
                    print_status("Archivos Q&A", "MISSING", "No hay archivos JSON de Q&A")
            else:
                print_status("Carpeta qa", "MISSING", "Crea: mkdir -p mvp/backend/content/qa")
                os.makedirs(qa_dir, exist_ok=True)
        else:
            print_status("Carpeta content", "MISSING", "Crea: mkdir -p mvp/backend/content")
            os.makedirs(content_dir, exist_ok=True)
        
        # Verificar servidor
        server_running = check_server_running()
        if server_running:
            print_status("Servidor FastAPI", "OK", "Ejecutándose en http://localhost:8000")
        else:
            print_status("Servidor FastAPI", "MISSING", "Inicia con: cd mvp/backend && uvicorn main:app --reload")
    else:
        print_status("Carpeta backend", "MISSING", "Crea: mkdir -p mvp/backend")
        os.makedirs(backend_dir, exist_ok=True)
    
    # Verificar Frontend
    print_header("FRONTEND")
    
    frontend_dir = os.path.join(mvp_dir, "frontend")
    if check_dir_exists(frontend_dir):
        print_status("Carpeta frontend", "OK")
        
        if check_file_exists(os.path.join(frontend_dir, "index.html")):
            print_status("index.html", "OK")
        else:
            print_status("index.html", "MISSING", "Página principal no encontrada")
        
        if check_file_exists(os.path.join(frontend_dir, "main.js")):
            print_status("main.js", "OK")
        else:
            print_status("main.js", "MISSING", "JavaScript principal no encontrado")
        
        if check_file_exists(os.path.join(frontend_dir, "style.css")):
            print_status("style.css", "OK")
        else:
            print_status("style.css", "MISSING", "Estilos CSS no encontrados")
    else:
        print_status("Carpeta frontend", "MISSING", "Crea: mkdir -p mvp/frontend")
        os.makedirs(frontend_dir, exist_ok=True)
    
    # Verificar AR
    print_header("REALIDAD AUMENTADA")
    
    ar_dir = os.path.join(mvp_dir, "ar")
    if check_dir_exists(ar_dir):
        print_status("Carpeta ar", "OK")
        
        if check_file_exists(os.path.join(ar_dir, "index.html")):
            print_status("index.html AR", "OK")
        else:
            print_status("index.html AR", "MISSING", "Implementación AR no encontrada")
    else:
        print_status("Carpeta ar", "MISSING", "Crea: mkdir -p mvp/ar")
        os.makedirs(ar_dir, exist_ok=True)
    
    # Verificar Documentación
    print_header("DOCUMENTACIÓN")
    
    if check_file_exists(os.path.join(docs_dir, "endpoints.md")):
        print_status("endpoints.md", "OK")
    else:
        print_status("endpoints.md", "MISSING", "Documentación de API no encontrada")
    
    if check_file_exists(os.path.join(docs_dir, "estructura_proyecto.md")):
        print_status("estructura_proyecto.md", "OK")
    else:
        print_status("estructura_proyecto.md", "MISSING", "Estructura del proyecto no documentada")
    
    # Verificar Scrum
    print_header("GESTIÓN SCRUM")
    
    sprints_dir = os.path.join(project_root, "sprints")
    backlog_file = os.path.join(project_root, "backlog.md")
    
    if check_dir_exists(sprints_dir):
        print_status("Carpeta sprints", "OK")
        sprint_count = len([f for f in os.listdir(sprints_dir) if f.endswith(".md")])
        print_status(f"Sprints definidos: {sprint_count}", "INFO" if sprint_count > 0 else "MISSING")
    else:
        print_status("Carpeta sprints", "MISSING", "Crea: mkdir -p sprints")
        os.makedirs(sprints_dir, exist_ok=True)
    
    if check_file_exists(backlog_file):
        print_status("backlog.md", "OK")
    else:
        print_status("backlog.md", "MISSING", "Product Backlog no encontrado")
    
    # Recomendaciones finales
    print_header("PRÓXIMOS PASOS RECOMENDADOS")
    
    if not check_file_exists(os.path.join(backend_dir, "main.py")):
        print("1. Implementar backend básico con FastAPI")
    elif not check_server_running():
        print("1. Iniciar el servidor backend con: cd mvp/backend && uvicorn main:app --reload")
    elif not check_file_exists(os.path.join(frontend_dir, "index.html")):
        print("1. Implementar frontend básico (HTML/CSS/JS)")
    elif not check_file_exists(os.path.join(ar_dir, "index.html")):
        print("1. Implementar prototipo AR básico (AR.js/A-Frame)")
    else:
        print("1. Mejorar la documentación y pruebas")
    
    # Mostrar mensajes de ayuda
    print("\nEjecuta este script regularmente para verificar el estado del proyecto.")
    print("Para iniciar un chat sobre un módulo específico, usa la plantilla chat_template.md")

if __name__ == "__main__":
    main()
