---
name: setup-portable
description: Instrucciones portátiles para configurar el proyecto en cualquier ordenador
metadata:
  type: reference
---

# Setup Portátil - Django CV Web App

## Para Reproducir en Otro Ordenador

### Requisitos Previos
- **Python 3.8+** instalado y en PATH
- **pip** (incluido con Python)
- **Git** (opcional, solo si clonaste desde repo)

### Pasos de Configuración

#### 1. Navega a la carpeta del proyecto
```powershell
cd "ruta\a\11202_PR01-main"
```

#### 2. Crea un virtual environment
```powershell
python -m venv venv
```

#### 3. Activa el virtual environment
```powershell
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (CMD)
venv\Scripts\activate.bat

# Linux/Mac
source venv/bin/activate
```

#### 4. Instala las dependencias
```powershell
pip install django==6.0.4
```

#### 5. Valida la configuración Django
```powershell
python manage.py check
```
Debería mostrar: "System check identified no issues (0 silenced)."

#### 6. Inicia el servidor de desarrollo
```powershell
python manage.py runserver
```

Deberías ver algo como:
```
Watching for file changes with StatReloader
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

#### 7. Accede a la aplicación
- **CV HTML:** http://localhost:8000/
- **CV JSON:** http://localhost:8000/api/cv/
- **Admin:** http://localhost:8000/admin/

### Solución de Problemas

**"ModuleNotFoundError: No module named 'django'"**
- Asegúrate de que el venv esté activado (`.\venv\Scripts\Activate.ps1`)
- Intenta reinstalar: `pip install django==6.0.4`

**"Port 8000 already in use"**
- Usa otro puerto: `python manage.py runserver 8001`

**"No such table" / errores de BD**
- La app no usa BD, puedes ignorar estos errores
- Si persisten, intenta: `python manage.py migrate`

**"template not found"**
- Verifica que exista: `cv/templates/cv/index.html`
- Valida con: `python manage.py check`

### Para Editores Recomendados
Si usas VS Code, instala extensiones:
- Python (Microsoft)
- Pylance
- Django (Baptiste Darthenay)

### Flujo de Desarrollo Típico

**1. Modificar datos del CV:**
```python
# cv/views.py - función get_cv_data()
# Edita el dict y guarda
# El servidor recargará automáticamente
```

**2. Modificar template:**
```html
<!-- cv/templates/cv/index.html -->
<!-- Edita y guarda, recarga navegador (Ctrl+R o F5) -->
```

**3. Modificar estilos/scripts:**
- Todo está dentro de `index.html` en tags `<style>` y `<script>`
- Edita, guarda y recarga navegador

**4. Exportar a PDF:**
- En la UI hay un botón "Descargar PDF"
- Usa html2canvas + jsPDF (librería CDN)
- Funciona en navegador, sin backend

### Comandos Útiles

```powershell
# Ver todos los endpoints
python manage.py show_urls

# Ejecutar shell interactivo Django
python manage.py shell

# Crear superuser (no necesario, pero útil)
python manage.py createsuperuser

# Limpiar caché
del /S __pycache__  # Windows
rm -rf **/__pycache__  # Linux/Mac
```

### Estructura de Archivos Clave

| Archivo | Propósito |
|---------|-----------|
| `cv/views.py` | Lógica + datos del CV (función `get_cv_data()`) |
| `cv/urls.py` | Rutas internas (`/` y `/api/cv/`) |
| `config/urls.py` | Rutas principales (incluye cv.urls) |
| `config/settings.py` | Configuración Django (DEBUG=True) |
| `cv/templates/cv/index.html` | Template principal (~1770 líneas) |
| `cv/templates/cv/github.html` | Template alternativo (no ruteado) |
| `static/foto.png` | Foto de perfil |

### Desactivar Virtual Environment
```powershell
deactivate
```

### Copiar a Otro Ordenador
Para hacer la app totalmente portátil:

1. **Copia solo esto** (excluyendo `venv/`):
```
11202_PR01-main/
├── cv/
├── config/
├── static/
├── manage.py
├── CLAUDE.md
└── [otros archivos EXCEPTO venv/ y db.sqlite3]
```

2. **En el nuevo ordenador:**
   - Sigue los pasos 1-6 arriba
   - El nuevo venv se creará limpio
   - Todas las dependencias se instalarán desde cero

3. **¿Preservar cambios no comiteados?**
   - Antes de copiar, crea un commit:
   ```powershell
   git add .
   git commit -m "Cambios antes de transportar"
   ```
   - Luego copia la carpeta completa (incluyendo `.git/`)
   - En el nuevo ordenador: `git status` debería mostrar limpio

### Variables de Entorno (Opcional)
Para producción, considera:
```powershell
# .env (crea este archivo en la raíz)
DEBUG=False
SECRET_KEY=tu-clave-secreta-larga
ALLOWED_HOSTS=localhost,127.0.0.1
```

Cargalas con `python-dotenv` si lo necesitas.

---

**Última actualización:** 2026-06-11
**Testeado en:** Windows 10, Python 3.x, Django 6.0.4
