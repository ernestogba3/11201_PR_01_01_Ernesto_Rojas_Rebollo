# CV Django Template - Guia de uso

Este proyecto renderiza un CV con Django usando una plantilla HTML dinamica.

## 1. Estructura principal

- Vista principal: `cv/views.py`
- Plantilla: `cv/templates/cv/index.html`
- Endpoint HTML: `/`
- Endpoint JSON: `/api/cv/`

La vista envia un diccionario `cv` con todos los bloques de datos.

## 2. Uso de etiquetas Django en la plantilla

### 2.1 Condicionales `{% if %}`

Se usan para mostrar campos opcionales solo cuando existe dato.

Ejemplo:

```django
{% if cv.personal_info.telefono2 %}
    <li>Telefono 2: {{ cv.personal_info.telefono2 }}</li>
{% endif %}
```

Otro ejemplo con campo booleano que puede ser `None`:

```django
{% if cv.personal_info.carnet_conducir is not None %}
    <li>Carnet conducir: {{ cv.personal_info.carnet_conducir|yesno:"Si,No" }}</li>
{% endif %}
```

### 2.2 Iteraciones `{% for %}`

Se usan para recorrer listas como experiencia, educacion, proyectos, etc.

Ejemplo:

```django
{% for item in cv.work_experience %}
    <article>
        <h3>{{ item.puesto }} - {{ item.empresa }}</h3>
    </article>
{% endfor %}
```

### 2.3 Variables `{{ ... }}`

Muestran valores enviados desde la vista.

Ejemplo:

```django
<p>{{ cv.personal_info.email_profesional1 }}</p>
```

### 2.4 Filtros (ejemplo: `yesno`)

Se usan para transformar valores al mostrar.

Ejemplo:

```django
{{ item.trabajo_actual|yesno:"Si,No" }}
```

## 3. Reglas recomendadas de contenido

1. Campos obligatorios: se muestran directamente.
2. Campos no obligatorios: envolver siempre con `{% if ... %}`.
3. Listas: renderizar con `{% for ... %}`.
4. Booleanos visibles: usar `|yesno:"Si,No"`.

## 4. Como agregar un nuevo campo

1. Agregar el dato en `get_cv_data()` dentro de `cv/views.py`.
2. Si es opcional, mostrarlo en template con `{% if campo %}`.
3. Si es lista, usar `{% for item in lista %}`.
4. Si es booleano, aplicar `|yesno:"Si,No"`.

## 5. Acordeon de secciones e items

La plantilla incluye JavaScript para:

- Convertir cada bloque `.section` en acordeon.
- Convertir cada `article` interno en subacordeon.
- Ocultar secciones vacias automaticamente.
- Abrir la primera seccion con contenido al cargar.

## 6. Selector de color de template

En el header hay un `select` (`#themeSelect`) que cambia colores del tema usando variables CSS:

- `--accent`
- `--accent-2`
- `--accent-rgb`
- `--accent-2-rgb`

La seleccion se guarda en `localStorage` con la clave `cv-theme`.

## 7. Ejecutar el proyecto

Desde la raiz del proyecto:

```powershell
c:/Proyectos/pr01/.venv/Scripts/python.exe manage.py runserver
```

Validacion rapida:

```powershell
c:/Proyectos/pr01/.venv/Scripts/python.exe manage.py check
```

## 8. Checklist rapido para mantener plantilla

- [ ] Campo opcional nuevo usa `{% if %}`
- [ ] Lista nueva usa `{% for %}`
- [ ] Booleanos visibles usan `yesno`
- [ ] No se muestran bloques vacios
- [ ] `manage.py check` sin errores
