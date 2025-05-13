#!/usr/bin/env python3
# generar_prompt.py - Genera un prompt personalizado para FRANKO.AR
# Adaptado al flujo de trabajo: Repo compartido = Estado local actual

import os
import sys
import subprocess
from datetime import datetime
import re
import argparse

def capturar_salida_comando(comando):
    """Ejecuta un comando y captura su salida como texto"""
    try:
        resultado = subprocess.run(comando, shell=True, check=True, 
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
                                  universal_newlines=True)
        return resultado.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar '{comando}': {e}")
        return f"Error: {e}"

def extraer_estado_actual():
    """Extrae información relevante del estado actual del proyecto"""
    # Ejecutar estado_frankoar.py y capturar su salida
    salida_estado = capturar_salida_comando("python estado_frankoar.py")

    # Extraer solo las partes relevantes (implementado/pendiente)
    estado_backend = []
    estado_frontend = []
    estado_ar = []
    proximos_pasos = []

    # Banderas para identificar secciones
    en_backend = False
    en_frontend = False
    en_ar = False
    en_proximos = False

    for linea in salida_estado.split('\n'):
        if "BACKEND" in linea:
            en_backend = True
            en_frontend = en_ar = en_proximos = False
            continue
        elif "FRONTEND" in linea:
            en_frontend = True
            en_backend = en_ar = en_proximos = False
            continue
        elif "REALIDAD AUMENTADA" in linea:
            en_ar = True
            en_backend = en_frontend = en_proximos = False
            continue
        elif "PRÓXIMOS PASOS" in linea:
            en_proximos = True
            en_backend = en_frontend = en_ar = False
            continue
        elif "DOCUMENTACIÓN" in linea or "GESTIÓN SCRUM" in linea:
            en_backend = en_frontend = en_ar = en_proximos = False
            continue

        # Capturar estados con ✅, ❌ o ⚠️
        if en_backend and ("✅" in linea or "❌" in linea or "⚠️" in linea):
            estado_backend.append(linea.strip())
        elif en_frontend and ("✅" in linea or "❌" in linea or "⚠️" in linea):
            estado_frontend.append(linea.strip())
        elif en_ar and ("✅" in linea or "❌" in linea or "⚠️" in linea):
            estado_ar.append(linea.strip())
        elif en_proximos and linea.strip() and linea.strip()[0].isdigit():
            proximos_pasos.append(linea.strip())

    # Limpiar los prefijos de estado y símbolos
    limpiar = lambda x: re.sub(r'[✅❌⚠️]\s*', '- ', x)
    estado_backend = [limpiar(x) for x in estado_backend]
    estado_frontend = [limpiar(x) for x in estado_frontend]
    estado_ar = [limpiar(x) for x in estado_ar]

    # Analizar main.py para detectar endpoints implementados
    backend_file = "mvp/backend/main.py"
    if os.path.exists(backend_file):
        with open(backend_file, 'r', encoding='utf-8') as f:
            contenido = f.read()
            endpoints = re.findall(r'@app\.(get|post|put|delete)\(.*?\)\s+async def ([^:]+):', contenido)
            for metodo, nombre in endpoints:
                estado_backend.append(f"- Endpoint {metodo.upper()} /{nombre} implementado")

    return {
        "backend": estado_backend,
        "frontend": estado_frontend,
        "ar": estado_ar,
        "proximos_pasos": proximos_pasos
    }

def obtener_tareas_sprint(sprint_file="sprints/sprint_1.md"):
    """Obtiene las tareas actuales del sprint"""
    if not os.path.exists(sprint_file):
        return ["Sprint file not found"]
    
    with open(sprint_file, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Extraer sección de elementos del backlog seleccionados
    match = re.search(r'## Elementos del Backlog Seleccionados\s+(.+?)(?=##)', contenido, re.DOTALL)
    if not match:
        return ["No se encontró sección de elementos del backlog"]
    
    tareas_texto = match.group(1).strip()
    
    # Extraer cada tarea
    tareas = []
    for tarea in re.finditer(r'### \d+\.\s+(.+?)(?=###|\Z)', tareas_texto, re.DOTALL):
        tareas.append(tarea.group(1).strip())
    
    # Si no se encontraron tareas con el patrón anterior, intentar otro formato
    if not tareas:
        tareas = [line.strip() for line in tareas_texto.split('\n') if line.strip().startswith('-')]
    
    return tareas

def obtener_daily_scrums(sprint_file="sprints/sprint_1.md"):
    """Obtiene los Daily Scrums registrados en el sprint"""
    if not os.path.exists(sprint_file):
        return []
    
    with open(sprint_file, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Extraer sección de Daily Scrums
    match = re.search(r'## Daily Scrums\s+(.+?)(?=##|\Z)', contenido, re.DOTALL)
    if not match:
        return []
    
    daily_texto = match.group(1).strip()
    
    # Extraer entradas de daily scrums
    dailies = []
    for daily in re.finditer(r'### Día \d+ - (.*?)\s+(.+?)(?=### Día|\Z)', daily_texto, re.DOTALL):
        fecha = daily.group(1).strip()
        contenido_daily = daily.group(2).strip()
        dailies.append({"fecha": fecha, "contenido": contenido_daily})
    
    return dailies

def obtener_ultimo_daily(sprint_file="sprints/sprint_1.md"):
    """Obtiene el último Daily Scrum registrado"""
    dailies = obtener_daily_scrums(sprint_file)
    if dailies:
        ultimo_daily = dailies[-1]
        # Extraer información clave del último daily
        completado = re.search(r'- \*\*Completado:\*\*\s+(.+?)\n', ultimo_daily['contenido'], re.DOTALL)
        por_hacer = re.search(r'- \*\*Por hacer hoy:\*\*\s+(.+?)\n', ultimo_daily['contenido'], re.DOTALL)
        impedimentos = re.search(r'- \*\*Impedimentos:\*\*\s+(.+?)\n', ultimo_daily['contenido'], re.DOTALL)
        return {
            "fecha": ultimo_daily['fecha'],
            "completado": completado.group(1).strip() if completado else "",
            "por_hacer": por_hacer.group(1).strip() if por_hacer else "",
            "impedimentos": impedimentos.group(1).strip() if impedimentos else ""
        }
    return None

def actualizar_daily_scrum(sprint_file="sprints/sprint_1.md"):
    """Añade una entrada de Daily Scrum al archivo del sprint"""
    if not os.path.exists(sprint_file):
        print(f"Error: No se encontró el archivo {sprint_file}")
        return False
    
    with open(sprint_file, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Determinar el número del próximo día
    dailies = obtener_daily_scrums(sprint_file)
    proximo_dia = len(dailies) + 1
    
    # Fecha actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    
    # Solicitar información del daily
    print(f"\n===== DAILY SCRUM - DÍA {proximo_dia} - {fecha_actual} =====\n")
    
    print("¿Qué completaste desde el último daily? (Escribe cada ítem y presiona Enter, línea vacía para terminar)")
    completado = []
    while True:
        item = input("> ")
        if not item:
            break
        completado.append(item)
    
    print("\n¿Qué harás hoy? (Escribe cada ítem y presiona Enter, línea vacía para terminar)")
    por_hacer = []
    while True:
        item = input("> ")
        if not item:
            break
        por_hacer.append(item)
    
    print("\n¿Hay algún impedimento? (Escribe cada ítem y presiona Enter, línea vacía para terminar)")
    impedimentos = []
    while True:
        item = input("> ")
        if not item:
            break
        impedimentos.append(item)
    
    # Crear texto del nuevo daily
    nuevo_daily = f"""
### Día {proximo_dia} - {fecha_actual}
- **Completado:** {", ".join(completado) if completado else "Ninguno"}
- **Por hacer hoy:** {", ".join(por_hacer) if por_hacer else "Ninguno"}
- **Impedimentos:** {", ".join(impedimentos) if impedimentos else "Ninguno"}
"""
    
    # Buscar sección de Daily Scrums
    match = re.search(r'## Daily Scrums\s+', contenido)
    if match:
        # Insertar nuevo daily después de la sección
        pos = match.end()
        nuevo_contenido = contenido[:pos] + nuevo_daily + contenido[pos:]
    else:
        # Si no existe la sección, buscar antes de Revisión del Sprint
        match = re.search(r'## Revisión del Sprint', contenido)
        if match:
            pos = match.start()
            nuevo_contenido = contenido[:pos] + "\n## Daily Scrums" + nuevo_daily + "\n" + contenido[pos:]
        else:
            # Si no hay sección de Revisión, añadir al final
            nuevo_contenido = contenido + "\n## Daily Scrums" + nuevo_daily
    
    # Guardar cambios
    with open(sprint_file, 'w', encoding='utf-8') as f:
        f.write(nuevo_contenido)
    
    print(f"\n✅ Daily Scrum registrado en {sprint_file}")
    return True

def generar_prompt(modulo="Backend", incluir_codigo=True):
    """Genera un prompt completo basado en el estado y el sprint"""
    estado = extraer_estado_actual()
    tareas_sprint = obtener_tareas_sprint()
    ultimo_daily = obtener_ultimo_daily()

    fecha_actual = datetime.now().strftime("%Y-%m-%d")

    # Determinar módulo y estado correspondiente
    if modulo.lower() == "backend":
        estado_modulo = estado["backend"]
        archivos_relevantes = [
            "- mvp/backend/main.py",
            "- mvp/backend/utils.py",
            "- mvp/backend/openai_conn.py",
            "- docs/endpoints.md"
        ]
    elif modulo.lower() == "frontend":
        estado_modulo = estado["frontend"]
        archivos_relevantes = [
            "- mvp/frontend/index.html",
            "- mvp/frontend/main.js",
            "- mvp/frontend/style.css"
        ]
    elif modulo.lower() == "ar":
        estado_modulo = estado["ar"]
        archivos_relevantes = [
            "- mvp/ar/index.html"
        ]
    else:
        estado_modulo = []
        archivos_relevantes = []

    # Determinar objetivo basado en el estado actual
    if modulo.lower() == "backend":
        if any("/personajes_cercanos" in paso for paso in estado["proximos_pasos"]):
            objetivo = "Implementar el endpoint de geolocalización POST /personajes_cercanos."
            limitaciones = [
                "- Debe usar el algoritmo Haversine para calcular distancias",
                "- Ordenar personajes por proximidad",
                "- Filtrar por radio (parámetro opcional)",
                "- Incluir documentación Swagger"
            ]
        elif any("/preguntar" in paso for paso in estado["proximos_pasos"]):
            objetivo = "Implementar el endpoint POST /preguntar para el sistema Q&A básico."
            limitaciones = [
                "- Buscar respuestas en archivos Q&A predefinidos",
                "- Sistema de fallback basado en keywords",
                "- Manejo de preguntas desconocidas",
                "- Incluir documentación Swagger"
            ]
        else:
            objetivo = "Revisar y optimizar los endpoints existentes."
            limitaciones = [
                "- Verificar manejo de errores",
                "- Añadir tests para cada endpoint",
                "- Mejorar documentación Swagger"
            ]
    elif modulo.lower() == "frontend":
        objetivo = "Implementar la funcionalidad de geolocalización en el frontend."
        limitaciones = [
            "- Solicitar permisos de ubicación al usuario",
            "- Enviar coordenadas al backend",
            "- Mostrar personajes cercanos",
            "- Indicador de carga mientras se buscan personajes"
        ]
    elif modulo.lower() == "ar":
        objetivo = "Crear estructura básica para AR.js/A-Frame."
        limitaciones = [
            "- Debe funcionar en navegadores móviles",
            "- Compatibilidad con AR.js y A-Frame",
            "- Preparado para mostrar avatar en coordenadas GPS"
        ]
    else:
        objetivo = "Por definir"
        limitaciones = []

    # Construir el prompt
    prompt = f"""PROYECTO: FRANKO.AR
MÓDULO: {modulo}
FECHA: {fecha_actual}

CONTEXTO IMPORTANTE: El estado que describo a continuación refleja mi entorno de desarrollo local actual. El repositorio que comparto contiene exactamente este mismo estado.

ESTADO ACTUAL:
"""

    # Agregar estado del módulo
    for item in estado_modulo:
        prompt += f"{item}\n"

    # Agregar información del último daily si existe
    if ultimo_daily:
        prompt += f"\nÚLTIMO DAILY SCRUM ({ultimo_daily['fecha']}):\n"
        prompt += f"- Último completado: {ultimo_daily['completado']}\n"
        prompt += f"- Planeado: {ultimo_daily['por_hacer']}\n"
        if ultimo_daily['impedimentos']:
            prompt += f"- Impedimentos: {ultimo_daily['impedimentos']}\n"

    prompt += f"""
ARCHIVOS RELEVANTES:
"""

    # Agregar archivos relevantes
    for archivo in archivos_relevantes:
        prompt += f"{archivo}\n"

    prompt += f"""
OBJETIVO DE ESTA SESIÓN:
{objetivo}

LIMITACIONES/REQUISITOS:
"""

    # Agregar limitaciones
    for item in limitaciones:
        prompt += f"{item}\n"

    prompt += f"""
TAREAS DEL SPRINT RELACIONADAS:
"""

    # Agregar tareas del sprint
    for tarea in tareas_sprint:
        descripcion = tarea.split('\n')[0].strip()
        prompt += f"- {descripcion}\n"

    return prompt

def main():
    # Configurar argumentos
    parser = argparse.ArgumentParser(description="Genera un prompt para ChatGPT/Claude basado en el estado del proyecto")
    parser.add_argument('modulo', nargs='?', default=None, choices=['Backend', 'Frontend', 'AR'], 
                        help='Módulo a trabajar (Backend, Frontend, AR)')
    parser.add_argument('--actualizar-daily', '-d', action='store_true',
                        help='Actualizar Daily Scrum antes de generar el prompt')
    parser.add_argument('--sin-codigo', '-s', action='store_true',
                        help='No incluir código actual en el prompt')
    args = parser.parse_args()
    
    # Actualizar Daily Scrum si se solicita
    if args.actualizar_daily:
        actualizar_daily_scrum()
    
    # Solicitar módulo si no se proporcionó
    modulo = args.modulo
    if not modulo:
        modulo = input("Ingresa el módulo (Backend/Frontend/AR): ")
    
    # Generar prompt
    prompt = generar_prompt(modulo, not args.sin_codigo)
    
    # Imprimir el prompt
    print("\n" + "="*50)
    print("PROMPT LISTO PARA USAR EN NUEVO CHAT:")
    print("="*50 + "\n")
    print(prompt)
    
    # Guardar en archivo
    nombre_archivo = f"prompt_{modulo.lower()}_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write(prompt)
    
    print(f"\nPrompt guardado en: {nombre_archivo}")
    print("Copia este contenido al iniciar un nuevo chat.")

if __name__ == "__main__":
    main()
