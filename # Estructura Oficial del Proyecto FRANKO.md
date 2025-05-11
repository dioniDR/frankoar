# Estructura Oficial del Proyecto FRANKO.AR

Este archivo define la estructura principal del proyecto. Todos los módulos, chats especializados y colaboradores deben organizar sus entregables siguiendo esta jerarquía. El objetivo es mantener un orden escalable, accesible y fácil de integrar.

---

## 📁 Raíz del proyecto: `frankoar/`

```
frankoar/
├── .gitignore
├── README.md
├── docs/
│   ├── guia_chats_modulares.md
│   ├── extensiones.md
│   ├── paper_frankoar.md
│   ├── estructura_proyecto.md ← (este archivo)
│   └── bibliografia.md
├── mvp/
│   ├── backend/
│   ├── frontend/
│   ├── content/
│   └── test_notes.md
├── core/
│   ├── api/
│   └── models/
├── interface/
│   ├── mobile_app/
│   ├── web_dashboard/
│   └── admin_panel/
├── content/
│   ├── ciudad_demo/
│   └── multimedia/
├── plugins/
│   ├── plugin_restaurante/
│   └── plugin_biblioteca/
├── data_collector/
│   ├── formularios/
│   ├── entrevistas/
│   └── procesamiento/
├── blog/
│   └── 2025-05-por-que-nace-frankoar.md
├── roadmap/
│   ├── fase_1_mvp.md
│   ├── fase_2_participacion.md
│   └── fase_3_escala_municipal.md
├── public/
├── scripts/
│   ├── deploy.sh
│   └── carga_inicial.py
└── demos/
    ├── backend_api_demo.zip
    ├── frontend_demo.zip
    └── contenido_minimo_demo.zip
```

---

## 🗂️ Descripción de carpetas principales

* `docs/`: Documentación técnica, estratégica y colaborativa.
* `mvp/`: Código y contenido mínimo del producto funcional.
* `core/`: Elementos generales del framework reutilizable.
* `interface/`: Diferentes versiones visuales del sistema.
* `content/`: Historias, datos culturales, multimedia.
* `plugins/`: Módulos opcionales según sectores (restaurantes, bibliotecas, etc.).
* `data_collector/`: Herramientas para recolectar y clasificar aportes ciudadanos.
* `blog/`: Entradas motivacionales y de avance del proyecto.
* `roadmap/`: Seguimiento por fases y visión a futuro.
* `public/`: Archivos accesibles para usuarios (web content, assets).
* `scripts/`: Automatización y despliegue.
* `demos/`: Resultados descargables (ZIPs) por módulo o chat.

---

## ⚠️ Reglas estructurales

* Ningún módulo debe crear carpetas fuera de esta jerarquía sin pasar por el coordinador (`FRANKO.AR Manager`).
* Toda entrega debe respetar su ruta definida.
* Las extensiones futuras deben documentarse en `/docs/extensiones.md`.
* Las actualizaciones a esta estructura deben registrarse y notificarse.

---

Este archivo se actualiza cuando cambia la estructura del sistema. Sirve como referencia para colaboradores humanos o módulos automatizados.
