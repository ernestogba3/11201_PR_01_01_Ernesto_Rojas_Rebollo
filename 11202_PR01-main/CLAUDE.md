# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Django-based CV/portfolio web application that renders a personal curriculum vitae as HTML with theme customization, accordion UI, and client-side PDF export. There is no database usage — all CV data is hardcoded in Python.

## Commands

```powershell
# Activate virtual environment (Windows)
.\venv\Scripts\Activate.ps1

# Run development server
python manage.py runserver

# Validate Django configuration
python manage.py check
```

**Endpoints:**
- `http://localhost:8000/` — HTML CV view (index.html template)
- `http://localhost:8000/api/cv/` — JSON API returning full CV data
- `http://localhost:8000/admin/` — Django admin

## Architecture

**Data flow:** `get_cv_data()` in [cv/views.py](cv/views.py) → context dict → Django template rendering. All CV content lives in that single function — it returns a hardcoded Python dictionary with sections: `personal_info`, `professional_profile`, `experiencias`, `education`, `complementary_training`, `skills`, `languages`, `projects`, `achievements`, `volunteering`, `social_network`, `interests`, `other_info`.

**No ORM:** `models.py` and `migrations/` are empty. The database file `db.sqlite3` exists but is unused.

**Two templates** in [cv/templates/cv/](cv/templates/cv/):
- `index.html` — main template (~1770 lines), custom dark/light design, routed at `/`
- `github.html` — GitHub-profile-styled alternative, not yet routed

**Frontend (in-template):** Vanilla JavaScript handles section visibility toggling, accordion expand/collapse, the theme switcher (reads/writes `localStorage`), and PDF export via `html2canvas` + `jsPDF` loaded from CDN.

**Theme system:** CSS custom properties (`--bg0`, `--t1`, `--a1`, etc.) are redefined per theme class on `<body>`. The selected theme persists in `localStorage`.

## Key Files

| File | Purpose |
|------|---------|
| [cv/views.py](cv/views.py) | All CV data + `cv_view` + `cv_json_view` |
| [cv/urls.py](cv/urls.py) | Routes: `""` → HTML, `api/cv/` → JSON |
| [config/urls.py](config/urls.py) | Includes cv.urls at root + admin |
| [config/settings.py](config/settings.py) | Django settings (DEBUG=True, SQLite) |
| [cv/templates/cv/index.html](cv/templates/cv/index.html) | Main rendered CV |
| [cv/templates/cv/github.html](cv/templates/cv/github.html) | GitHub-style alternate CV |
| [static/foto.png](static/foto.png) | Profile photo |

## Modifying CV Content

Edit the `get_cv_data()` function in [cv/views.py](cv/views.py). The dict keys map 1:1 to Django template variables. Adding a new top-level key requires adding it to the context dict in `cv_view()` and referencing it in the template with `{{ key }}` or `{% for item in key %}`.

## Adding a New Template Route

1. Add a new view function in [cv/views.py](cv/views.py) that calls `render(request, 'cv/your_template.html', context)`
2. Add the URL pattern in [cv/urls.py](cv/urls.py)
3. Create the template at `cv/templates/cv/your_template.html`

## Stack

- Django 6.0.4 / Python
- SQLite (present but unused)
- Vanilla JS (no npm, no bundler)
- html2canvas + jsPDF (CDN, client-side PDF export)
- CSS custom properties for theming
