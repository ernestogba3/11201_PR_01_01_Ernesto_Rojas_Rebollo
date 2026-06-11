---
name: quick-reference
description: Referencia rápida - comandos, archivos clave, endpoints
metadata:
  type: reference
---

# Quick Reference - Django CV App

## Comandos Rápidos

```powershell
# Activar venv
.\venv\Scripts\Activate.ps1

# Instalar dependencias
pip install django==6.0.4

# Validar setup
python manage.py check

# Iniciar servidor
python manage.py runserver

# Ejecutar shell
python manage.py shell

# Deactivar venv
deactivate
```

## Archivos Clave para Editar

| Archivo | Qué cambiar |
|---------|------------|
| `cv/views.py` | Contenido del CV (función `get_cv_data()`) |
| `cv/templates/cv/index.html` | Estructura, estilos, scripts del template |
| `cv/urls.py` | Rutas internas |
| `static/foto.png` | Foto de perfil |

## Endpoints

| URL | Descripción |
|-----|-------------|
| `http://localhost:8000/` | CV en HTML (template index.html) |
| `http://localhost:8000/api/cv/` | Data del CV en JSON |
| `http://localhost:8000/admin/` | Panel de admin (no usado) |

## Estructura de get_cv_data()

```python
{
    "curriculum_vitae": {...},    # Metadata
    "personal_info": {...},       # Nombre, email, teléfono, ubicación
    "professional_profile": {...},# Profesión, objetivo, resumen
    "experiencias": [...],        # Historial laboral
    "education": [...],           # Formación académica
    "complementary_training": [...], # Cursos
    "skills": [...],              # Habilidades
    "languages": [...],           # Idiomas
    "projects": [...],            # Proyectos personales
    "achievements": [...],        # Logros
    "volunteering": [...],        # Voluntariado
    "social_network": [...],      # Links (LinkedIn, GitHub, etc.)
    "interests": [...],           # Intereses
    "other_info": {...}           # Datos varios
}
```

## Rutas (cv/urls.py)

```python
path('', cv_view, name='cv'),           # GET / → HTML
path('api/cv/', cv_json_view, name='api_cv'),  # GET /api/cv/ → JSON
```

## Temas (Themes)

- **Activos:** dark, light
- **Almacenaje:** localStorage (clave: "theme")
- **Archivo:** Todo en index.html (CSS custom properties)

## Estado Actual (2026-06-11)

✅ Funcional:
- Template index.html
- Tema dark/light
- PDF export
- Acordeón UI
- Validador de curriculums

⚠️ Pendiente:
- Template github.html (no ruteado)
- Cambios sin comitear

## Stack

- Django 6.0.4
- Python 3.x
- Vanilla JS (sin frameworks)
- SQLite (presente pero sin usar)
- html2canvas + jsPDF (CDN para PDF)

## Para Copiar a Otro PC

Copia solo (excluyendo `venv/`):
```
cv/
config/
static/
manage.py
CLAUDE.md
.git/
```

Luego en el nuevo PC:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install django==6.0.4
python manage.py check
python manage.py runserver
```

## Contacto del Usuario

- Email: ernestogba2@gmail.com
- Ubicación del workspace: 
  ```
  c:\Users\err-r\Desktop\Curso de programacion 2026\
  Clones de GitHub\Practicas_Curriculum\
  11201_PR_01_01_Ernesto_Rojas_Rebollo\11202_PR01-main\
  ```

---

**Última actualización:** 2026-06-11
