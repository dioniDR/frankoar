#!/usr/bin/env python3
# scrum_manager.py - Gestor de Scrum para FRANKO.AR

import os
import json
import datetime
import sys
from pathlib import Path

# Configuración
SPRINT_FOLDER = 'sprints'
CURRENT_SPRINT_FILE = '.current_sprint'
BACKLOG_FILE = 'backlog.md'

def crear_carpeta_sprints():
    """Crea la carpeta de sprints si no existe"""
    if not os.path.exists(SPRINT_FOLDER):
        os.makedirs(SPRINT_FOLDER)
        print(f"✅ Carpeta '{SPRINT_FOLDER}' creada")

def obtener_sprint_actual():
    """Obtiene el número del sprint actual"""
    if os.path.exists(CURRENT_SPRINT_FILE):
        with open(CURRENT_SPRINT_FILE, 'r') as f:
            return int(f.read().strip())
    return 0

def guardar_sprint_actual(num_sprint):
    """Guarda el número del sprint actual"""
    with open(CURRENT_SPRINT_FILE, 'w') as f:
        f.write(str(num_sprint))

def iniciar_sprint(num_sprint, duracion_dias=7):
    """Inicia un nuevo sprint"""
    crear_carpeta_sprints()
    
    # Fecha de inicio y fin
    fecha_inicio = datetime.datetime.now()
    fecha_fin = fecha_inicio + datetime.timedelta(days=duracion_dias)
    
    # Crear archivo de sprint
    sprint_data = {
        "numero": num_sprint,
        "fecha_inicio": fecha_inicio.strftime("%Y-%m-%d"),
        "fecha_fin": fecha_fin.strftime("%Y-%m-%d"),
        "duracion_dias": duracion_dias,
        "objetivo": "",
        "tareas": [],
        "daily_scrums": [],
        "completado": False
    }
    
    sprint_file = os.path.join(SPRINT_FOLDER, f'sprint_{num_sprint}.json')
    with open(sprint_file, 'w') as f:
        json.dump(sprint_data, f, indent=2)
    
    guardar_sprint_actual(num_sprint)
    
    # Crear template para sprint backlog
    sprint_backlog_file = os.path.join(SPRINT_FOLDER, f'sprint_{num_sprint}_backlog.md')
    with open(sprint_backlog_file, 'w') as f:
        f.write(f"# Sprint {num_sprint} Backlog\n\n")
        f.write(f"**Fecha**: {fecha_inicio.strftime('%d-%m-%Y')} a {fecha_fin.strftime('%d-%m-%Y')}\n\n")
        f.write("**Objetivo del Sprint**: [Definir objetivo]\n\n")
        f.write("## Tareas\n\n")
        f.write("1. [ ] Tarea 1\n")
        f.write("   - [ ] Subtarea 1.1\n")
        f.write("   - [ ] Subtarea 1.2\n\n")
        f.write("2. [ ] Tarea 2\n")
        f.write("   - [ ] Subtarea 2.1\n")
        f.write("   - [ ] Subtarea 2.2\n\n")
    
    print(f"✅ Sprint {num_sprint} iniciado: {fecha_inicio.strftime('%d-%m-%Y')} a {fecha_fin.strftime('%d-%m-%Y')}")
    print(f"📝 Edita el archivo {sprint_backlog_file} para definir las tareas del sprint")

def registro_daily():
    """Registra un daily scrum"""
    sprint_actual = obtener_sprint_actual()
    if sprint_actual == 0:
        print("❌ No hay un sprint activo. Inicia uno con: python scrum_manager.py iniciar")
        return
    
    sprint_file = os.path.join(SPRINT_FOLDER, f'sprint_{sprint_actual}.json')
    if not os.path.exists(sprint_file):
        print(f"❌ Archivo de sprint {sprint_file} no encontrado")
        return
    
    # Cargar datos del sprint
    with open(sprint_file, 'r') as f:
        sprint_data = json.load(f)
    
    # Fecha actual
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Preguntar información del daily
    print(f"\n===== DAILY SCRUM - SPRINT {sprint_actual} - {fecha_actual} =====\n")
    
    print("¿Qué completaste ayer? (Escribe cada ítem y presiona Enter, línea vacía para terminar)")
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
    
    # Guardar daily scrum
    daily_data = {
        "fecha": fecha_actual,
        "completado": completado,
        "por_hacer": por_hacer,
        "impedimentos": impedimentos
    }
    
    sprint_data["daily_scrums"].append(daily_data)
    
    # Guardar datos actualizados
    with open(sprint_file, 'w') as f:
        json.dump(sprint_data, f, indent=2)
    
    # Crear archivo de daily para chatgpt
    daily_file = os.path.join(SPRINT_FOLDER, f'daily_{sprint_actual}_{fecha_actual}.md')
    with open(daily_file, 'w') as f:
        f.write(f"# Daily Scrum - Sprint {sprint_actual} - {fecha_actual}\n\n")
        
        f.write("## Completado ayer\n")
        for item in completado:
            f.write(f"- {item}\n")
        
        f.write("\n## Por hacer hoy\n")
        for item in por_hacer:
            f.write(f"- {item}\n")
        
        f.write("\n## Impedimentos\n")
        if impedimentos:
            for item in impedimentos:
                f.write(f"- {item}\n")
        else:
            f.write("- Ninguno\n")
    
    print(f"\n✅ Daily Scrum registrado en {daily_file}")
    print(f"📋 Usa este archivo para iniciar tu sesión con ChatGPT")

def finalizar_sprint():
    """Finaliza el sprint actual y genera el informe"""
    sprint_actual = obtener_sprint_actual()
    if sprint_actual == 0:
        print("❌ No hay un sprint activo. Inicia uno con: python scrum_manager.py iniciar")
        return
    
    sprint_file = os.path.join(SPRINT_FOLDER, f'sprint_{sprint_actual}.json')
    if not os.path.exists(sprint_file):
        print(f"❌ Archivo de sprint {sprint_file} no encontrado")
        return
    
    # Cargar datos del sprint
    with open(sprint_file, 'r') as f:
        sprint_data = json.load(f)
    
    # Preguntar información de la revisión
    print(f"\n===== REVISIÓN SPRINT {sprint_actual} =====\n")
    
    print("Elementos completados (Escribe cada ítem y presiona Enter, línea vacía para terminar)")
    completado = []
    while True:
        item = input("> ")
        if not item:
            break
        completado.append(item)
    
    print("\nElementos pendientes (Escribe cada ítem y presiona Enter, línea vacía para terminar)")
    pendiente = []
    while True:
        item = input("> ")
        if not item:
            break
        pendiente.append(item)
    
    print("\nAprendizajes (Escribe cada ítem y presiona Enter, línea vacía para terminar)")
    aprendizajes = []
    while True:
        item = input("> ")
        if not item:
            break
        aprendizajes.append(item)
    
    # Guardar revisión
    sprint_data["completado"] = True
    sprint_data["revision"] = {
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d"),
        "completado": completado,
        "pendiente": pendiente,
        "aprendizajes": aprendizajes
    }
    
    # Guardar datos actualizados
    with open(sprint_file, 'w') as f:
        json.dump(sprint_data, f, indent=2)
    
    # Crear archivo de revisión para chatgpt
    revision_file = os.path.join(SPRINT_FOLDER, f'revision_sprint_{sprint_actual}.md')
    with open(revision_file, 'w') as f:
        f.write(f"# Revisión Sprint {sprint_actual}\n\n")
        f.write(f"**Fecha**: {sprint_data['fecha_inicio']} a {sprint_data['fecha_fin']}\n\n")
        
        f.write("## Elementos completados\n")
        for item in completado:
            f.write(f"- {item}\n")
        
        f.write("\n## Elementos pendientes\n")
        for item in pendiente:
            f.write(f"- {item}\n")
        
        f.write("\n## Aprendizajes\n")
        for item in aprendizajes:
            f.write(f"- {item}\n")
    
    print(f"\n✅ Revisión del Sprint {sprint_actual} generada en {revision_file}")
    
    # Preguntar retrospectiva
    print(f"\n===== RETROSPECTIVA SPRINT {sprint_actual} =====\n")
    
    print("Lo que funcionó bien (Escribe cada ítem y presiona Enter, línea vacía para terminar)")
    bien = []
    while True:
        item = input("> ")
        if not item:
            break
        bien.append(item)
    
    print("\nLo que puede mejorar (Escribe cada ítem y presiona Enter, línea vacía para terminar)")
    mejorar = []
    while True:
        item = input("> ")
        if not item:
            break
        mejorar.append(item)
    
    print("\nAcciones para el próximo sprint (Escribe cada ítem y presiona Enter, línea vacía para terminar)")
    acciones = []
    while True:
        item = input("> ")
        if not item:
            break
        acciones.append(item)
    
    # Guardar retrospectiva
    sprint_data["retrospectiva"] = {
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d"),
        "bien": bien,
        "mejorar": mejorar,
        "acciones": acciones
    }
    
    # Guardar datos actualizados
    with open(sprint_file, 'w') as f:
        json.dump(sprint_data, f, indent=2)
    
    # Crear archivo de retrospectiva para chatgpt
    retro_file = os.path.join(SPRINT_FOLDER, f'retrospectiva_sprint_{sprint_actual}.md')
    with open(retro_file, 'w') as f:
        f.write(f"# Retrospectiva Sprint {sprint_actual}\n\n")
        
        f.write("## Lo que funcionó bien\n")
        for item in bien:
            f.write(f"- {item}\n")
        
        f.write("\n## Lo que puede mejorar\n")
        for item in mejorar:
            f.write(f"- {item}\n")
        
        f.write("\n## Acciones para el próximo sprint\n")
        for item in acciones:
            f.write(f"- {item}\n")
    
    print(f"\n✅ Retrospectiva del Sprint {sprint_actual} generada en {retro_file}")
    print(f"\n🎉 Sprint {sprint_actual} finalizado")
    
    # Iniciar siguiente sprint?
    siguiente = input("\n¿Quieres iniciar el siguiente sprint? (s/n): ")
    if siguiente.lower() == 's':
        iniciar_sprint(sprint_actual + 1)

def mostrar_estado():
    """Muestra el estado actual del sprint"""
    sprint_actual = obtener_sprint_actual()
    if sprint_actual == 0:
        print("❌ No hay un sprint activo. Inicia uno con: python scrum_manager.py iniciar")
        return
    
    sprint_file = os.path.join(SPRINT_FOLDER, f'sprint_{sprint_actual}.json')
    if not os.path.exists(sprint_file):
        print(f"❌ Archivo de sprint {sprint_file} no encontrado")
        return
    
    # Cargar datos del sprint
    with open(sprint_file, 'r') as f:
        sprint_data = json.load(f)
    
    fecha_inicio = sprint_data["fecha_inicio"]
    fecha_fin = sprint_data["fecha_fin"]
    duracion = sprint_data["duracion_dias"]
    
    # Calcular días restantes
    fecha_fin_obj = datetime.datetime.strptime(fecha_fin, "%Y-%m-%d")
    dias_restantes = (fecha_fin_obj - datetime.datetime.now()).days + 1
    
    print(f"\n===== ESTADO DEL SPRINT {sprint_actual} =====\n")
    print(f"Fecha inicio: {fecha_inicio}")
    print(f"Fecha fin: {fecha_fin}")
    print(f"Duración: {duracion} días")
    print(f"Días restantes: {dias_restantes if dias_restantes > 0 else 0}")
    
    # Mostrar daily scrums
    if "daily_scrums" in sprint_data and sprint_data["daily_scrums"]:
        print(f"\nDaily Scrums registrados: {len(sprint_data['daily_scrums'])}")
        
        # Mostrar último daily
        ultimo_daily = sprint_data["daily_scrums"][-