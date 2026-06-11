---
name: project-status-cv-app
description: Estado actual del proyecto Django CV webapp - estructura, progreso, y siguiente pasos
metadata:
  type: project
---

# Proyecto: Django CV Web App

## Descripción General
Aplicación web Django que renderiza un curriculum vitae personal como HTML con:
- Temas personalizables (dark/light)
- Interfaz acordeón para expandir/contraer secciones
- Exportación a PDF client-side (html2canvas + jsPDF)
- API JSON para obtener datos del CV
- Sin base de datos — todos los datos están hardcodeados en Python

## Stack Actual
- **Backend:** Django 6.0.4 / Python 3.x
- **BD:** SQLite (presente pero NO utilizado — no hay ORM)
- **Frontend:** Vanilla JavaScript (sin npm, sin bundler)
- **Librerías CDN:** html2canvas + jsPDF (para PDF export)
- **Estilos:** CSS custom properties para theming

## Estructura de Directorios
```
11202_PR01-main/
├── config/              # Configuración Django
│   ├── settings.py
│   ├── urls.py         # Rutas principales
│   └── wsgi.py
├── cv/                 # App Django principal
│   ├── views.py        # Toda la lógica: get_cv_data(), cv_view, cv_json_view
│   ├── urls.py         # Rutas internas
│   ├── models.py       # VACÍO - no se usa ORM
│   ├── migrations/     # VACÍO
│   ├── admin.py
│   └── templates/cv/
│       ├── index.html    # Template principal (~1770 líneas, tema dark/light integrado)
│       └── github.html   # Template alternativa estilo GitHub (no ruteada aún)
├── static/
│   └── foto.png        # Foto de perfil
├── templates/
├── db.sqlite3          # Presente pero SIN USAR
├── manage.py
├── CLAUDE.md           # Documentación del proyecto
└── venv/               # Virtual environment
```

## Flujo de Datos
1. `get_cv_data()` en cv/views.py → dict Python hardcodeado
2. `cv_view()` renderiza template con ese dict como context
3. Django inyecta en index.html como variables `{{ }}`
4. JavaScript vanilla maneja: tema, acordeón, PDF export

## Estructura de Datos (get_cv_data)
El dict retornado contiene estas keys principales:
- `curriculum_vitae` — metadata (user, created_at, updated_at)
- `personal_info` — nombre, email, teléfono, ciudad, etc.
- `professional_profile` — profesión, objetivo, resumen
- `experiencias` — lista de trabajos anteriores
- `education` — formación académica
- `complementary_training` — cursos, certificados
- `skills` — habilidades técnicas/soft
- `languages` — idiomas
- `projects` — proyectos personales
- `achievements` — logros y reconocimientos
- `volunteering` — voluntariado
- `social_network` — links a redes (LinkedIn, GitHub, etc.)
- `interests` — intereses personales
- `other_info` — datos adicionales

Todas las keys excepto `curriculum_vitae` tienen un subfield `"cv": "maria-perez-cv"` como referencia.

## Endpoints Actuales
- `http://localhost:8000/` → HTML CV (index.html)
- `http://localhost:8000/api/cv/` → JSON con toda la data
- `http://localhost:8000/admin/` → Django admin

## Temas (Themes)
Implementados en CSS custom properties en body:
- Variables: `--bg0`, `--t1`, `--a1`, etc.
- Redefinidas por clase en `<body class="theme-dark">` o `<body class="theme-light">`
- Persistencia: `localStorage` (lector/escritor en JS vanilla)
- Switcher: botón en header que cambia clase + guarda en localStorage

## Estado del Proyecto (2026-06-11)
**Último commit:** 56788b4 - "Añadido Validador de curriculums y comprobado con exito cv github"

**Cambios sin comitear:**
- M cv/templates/cv/index.html
- M ../cv-github.html
- ?? CLAUDE.md
- ?? cv/templates/cv/index2.html

**Progreso:**
✅ Template index.html funcional
✅ Template github.html creada (no ruteada)
✅ Tema dark/light con persistencia
✅ PDF export (client-side)
✅ Acordeón UI
✅ Validador de curriculums implementado
⚠️ Template github.html aún no tiene ruta asignada
⚠️ Hay cambios sin comitear que revisar

## Para Reproducir en Otro Ordenador
**Requisitos:**
- Python 3.x
- pip

**Setup:**
```powershell
# 1. Clonar repo / copiar carpeta

# 2. Crear virtual environment
python -m venv venv

# 3. Activar venv
.\venv\Scripts\Activate.ps1

# 4. Instalar dependencias
pip install django==6.0.4

# 5. Validar setup
python manage.py check

# 6. Iniciar servidor
python manage.py runserver

# 7. Acceder
# Abrir http://localhost:8000/
```

## Modificaciones Frecuentes
**Para cambiar contenido del CV:**
- Editar función `get_cv_data()` en cv/views.py
- Los dict keys mapean 1:1 con variables del template

**Para agregar nueva plantilla:**
1. Crear view en cv/views.py que renderice template nuevo
2. Agregar URL pattern en cv/urls.py
3. Crear template en cv/templates/cv/nombre.html

## Notas Importantes
- No hay migraciones de BD — la app no usa ORM
- Todos los datos están en memoria (python dict)
- No hay autenticación ni usuarios — es una app estática
- El validador de curriculums está en la app (checkea datos de CV)
- CSS personalizado en index.html (no hay archivo CSS separado)
- JavaScript dentro de `<script>` tags en template (no modularizado)

## Próximos Pasos Sugeridos
1. ✅ Comitear cambios sin comitear (index.html, index2.html, cv-github.html)
2. ⚠️ Decidir si github.html debe tener su propia ruta o ser alternativa switcheable
3. 📋 Posible refactoring: separar CSS y JS a archivos independientes
4. 📋 Añadir más temas (sepia, high-contrast, etc.)
5. 📋 Mejorar responsive design para móvil
