from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime


def get_cv_data():
    data = {
        "curriculum_vitae": {
            "user": "maria.perez",
            "created_at": "2026-04-26T10:00:00Z",
            "updated_at": "2026-04-26T10:00:00Z",
        },
        "personal_info": {
            "cv": "maria-perez-cv",
            "nombre": "Maria",
            "apellidos": "Perez Lopez",
            "nombre_completo": "Maria Perez Lopez",
            "telefono1": "+34 600 123 456",
            "telefono2": "+34 600 654 321",
            "email_profesional1": "maria.perez@email.com",
            "email_profesional2": "maria.perez.dev@email.com",
            "ciudad": "Madrid",
            "pais": "Espana",
            "codigo_postal": "28001",
            "fecha_nacimiento": "1998-06-12",
            "nacionalidad": "Espanola",
            "carnet_conducir": True,
            "disponibilidad": "Inmediata",
            "foto": "/static/foto.png",
        },
        "professional_profile": {
            "cv": "maria-perez-cv",
            "profesion": "Desarrolladora Full Stack e IA",
            "objetivo": "Aportar valor en productos digitales con frontend, backend e inteligencia artificial aplicada.",
            "resumen": "Perfil tecnico con experiencia construyendo interfaces modernas, APIs escalables y soluciones de IA para automatizacion.",
        },
        "experiencias": [
            {
                "cv": "maria-perez-cv",
                "puesto": "Frontend Developer",
                "company": "Pixel Studio",
                "empresa": "Pixel Studio",
                "ubicacion": "Barcelona",
                "fecha_inicio": datetime.strptime("2021-02-01", "%Y-%m-%d").date(),
                "fecha_fin": datetime.strptime("2022-08-30", "%Y-%m-%d").date(),
                "trabajo_actual": False,
                "descripcion": "Desarrollo de componentes UI y optimizacion de experiencia en aplicaciones SPA.",
                "logros": "Reduccion del tiempo de carga en 35% y mejora de accesibilidad AA.",
                "orden": 1,
            },
            {
                "cv": "maria-perez-cv",
                "puesto": "Backend Developer",
                "company": "DataCloud",
                "empresa": "DataCloud",
                "ubicacion": "Remoto",
                "fecha_inicio": datetime.strptime("2022-09-01", "%Y-%m-%d").date(),
                "fecha_fin": datetime.strptime("2024-01-15", "%Y-%m-%d").date(),
                "trabajo_actual": False,
                "descripcion": "Diseno e implementacion de APIs REST y procesamiento de datos en segundo plano.",
                "logros": "Disminucion de errores en produccion en 42% con observabilidad y testing.",
                "orden": 2,
            },
            {
                "cv": "maria-perez-cv",
                "puesto": "AI Engineer",
                "company": "NTEC AI Lab",
                "empresa": "NTEC AI Lab",
                "ubicacion": "Madrid",
                "fecha_inicio": datetime.strptime("2024-02-01", "%Y-%m-%d").date(),
                "fecha_fin": None,
                "trabajo_actual": True,
                "descripcion": "Integracion de modelos NLP y agentes para automatizar analisis y soporte interno.",
                "logros": "Ahorro de 280 horas/mes en tareas repetitivas mediante asistentes de IA.",
                "orden": 3,
            },
        ],
        "education": [
            {
                "cv": "maria-perez-cv",
                "titulo": "Ingenieria Electrica",
                "centro": "Universidad Tecnologica",
                "ubicacion": "Valencia",
                "fecha_inicio": datetime.strptime("1991-01-01", "%Y-%m-%d").date(),
                "fecha_fin": datetime.strptime("1996-12-31", "%Y-%m-%d").date(),
                "en_curso": False,
                "orden": 1,
            },
            {
                "cv": "maria-perez-cv",
                "titulo": "Bioinformatico",
                "centro": "Instituto Superior de Biociencias",
                "ubicacion": "Barcelona",
                "fecha_inicio": datetime.strptime("2019-01-01", "%Y-%m-%d").date(),
                "fecha_fin": datetime.strptime("2020-12-31", "%Y-%m-%d").date(),
                "en_curso": False,
                "orden": 2,
            }
        ],
        "complementary_training": [
            {
                "cv": "maria-perez-cv",
                "tipo": "Curso",
                "nombre": "Django REST Framework",
                "entidad": "Platzi",
                "fecha": datetime.strptime("2024-11-20", "%Y-%m-%d").date(),
                "descripcion": "Diseno y desarrollo de APIs REST.",
                "orden": 1,
            },
            {
                "cv": "maria-perez-cv",
                "tipo": "Bootcamp",
                "nombre": "Frontend avanzado con React",
                "entidad": "KeepCoding",
                "fecha": datetime.strptime("2023-06-10", "%Y-%m-%d").date(),
                "descripcion": "Arquitectura frontend, testing y performance web.",
                "orden": 2,
            },
            {
                "cv": "maria-perez-cv",
                "tipo": "Certificacion",
                "nombre": "Machine Learning Engineer",
                "entidad": "Coursera",
                "fecha": datetime.strptime("2025-03-15", "%Y-%m-%d").date(),
                "descripcion": "Modelado supervisado, MLOps basico e integracion en productos.",
                "orden": 3,
            },
            {
                "cv": "maria-perez-cv",
                "tipo": "Taller",
                "nombre": "Arquitectura de microservicios",
                "entidad": "NTEC Academy",
                "fecha": datetime.strptime("2024-09-12", "%Y-%m-%d").date(),
                "descripcion": "Patrones de resiliencia, colas y escalado horizontal.",
                "orden": 4,
            }
        ],
        "skills": [
            {
                "cv": "maria-perez-cv",
                "tipo": "Tecnica",
                "categoria": "Backend",
                "nombre": "Django",
                "nivel": 4,
                "orden": 1,
            },
            {
                "cv": "maria-perez-cv",
                "tipo": "Tecnica",
                "categoria": "Frontend",
                "nombre": "JavaScript",
                "nivel": 3,
                "orden": 2,
            },
            {
                "cv": "maria-perez-cv",
                "tipo": "Tecnica",
                "categoria": "IA",
                "nombre": "Prompt Engineering",
                "nivel": 4,
                "orden": 3,
            },
            {
                "cv": "maria-perez-cv",
                "tipo": "SoftSkill",
                "categoria": "Comunicacion",
                "nombre": "Trabajo en equipo",
                "nivel": 5,
                "orden": 4,
            },
            {
                "cv": "maria-perez-cv",
                "tipo": "SoftSkill",
                "categoria": "Liderazgo",
                "nombre": "Mentoria tecnica",
                "nivel": 4,
                "orden": 5,
            }
        ],
        "languages": [
            {
                "cv": "maria-perez-cv",
                "idioma": "Espanol",
                "nivel": "Nativo",
                "certificacion": "N/A",
                "orden": 1,
            },
            {
                "cv": "maria-perez-cv",
                "idioma": "Ingles",
                "nivel": "B2",
                "certificacion": "Cambridge First",
                "orden": 2,
            },
            {
                "cv": "maria-perez-cv",
                "idioma": "Catalan",
                "nivel": "B1",
                "certificacion": "N/A",
                "orden": 3,
            }
        ],
        "projects": [
            {
                "cv": "maria-perez-cv",
                "nombre": "CV Builder",
                "descripcion": "Aplicacion para gestionar perfiles profesionales.",
                "tecnologias": "Django, SQLite, HTML, CSS",
                "link": "https://github.com/example/cv-builder",
                "orden": 1,
            },
            {
                "cv": "maria-perez-cv",
                "nombre": "Smart Ticket Classifier",
                "descripcion": "Sistema de clasificacion automatica de incidencias con NLP.",
                "tecnologias": "Python, FastAPI, Transformers",
                "link": "https://github.com/example/smart-ticket-classifier",
                "orden": 2,
            },
            {
                "cv": "maria-perez-cv",
                "nombre": "Realtime Monitoring Dashboard",
                "descripcion": "Panel en tiempo real para metricas de negocio y sistema.",
                "tecnologias": "React, WebSocket, Node.js",
                "link": "https://github.com/example/realtime-monitoring-dashboard",
                "orden": 3,
            },
            {
                "cv": "maria-perez-cv",
                "nombre": "BioData Explorer",
                "descripcion": "Visualizacion y analisis de datos bioinformaticos.",
                "tecnologias": "Python, Pandas, Plotly",
                "link": "https://github.com/example/biodata-explorer",
                "orden": 4,
            }
        ],
        "achievements": [
            {
                "cv": "maria-perez-cv",
                "titulo": "Top Performer",
                "tipo": "Reconocimiento",
                "descripcion": "Reconocimiento por impacto en proyecto interno.",
                "fecha": datetime.strptime("2025-12-10", "%Y-%m-%d").date(),
                "orden": 1,
            },
            {
                "cv": "maria-perez-cv",
                "titulo": "Premio Innovacion IA",
                "tipo": "Premio",
                "descripcion": "Desarrollo de asistente inteligente para operaciones internas.",
                "fecha": datetime.strptime("2025-06-01", "%Y-%m-%d").date(),
                "orden": 2,
            },
            {
                "cv": "maria-perez-cv",
                "titulo": "Speaker en conferencia Tech",
                "tipo": "Conferencia",
                "descripcion": "Ponencia sobre arquitectura full stack y IA aplicada.",
                "fecha": datetime.strptime("2024-10-22", "%Y-%m-%d").date(),
                "orden": 3,
            },
            {
                "cv": "maria-perez-cv",
                "titulo": "Mejora continua de plataforma",
                "tipo": "Impacto",
                "descripcion": "Reduccion de latencia media en 40% en servicios criticos.",
                "fecha": datetime.strptime("2023-11-05", "%Y-%m-%d").date(),
                "orden": 4,
            }
        ],
        "volunteering": [
            {
                "cv": "maria-perez-cv",
                "organizacion": "Code for Good",
                "funcion": "Mentora",
                "impacto": "Formacion basica en programacion para jovenes.",
                "fecha_inicio": datetime.strptime("2024-01-01", "%Y-%m-%d").date(),
                "fecha_fin": None,
                "en_curso": True,
                "orden": 1,
            },
            {
                "cv": "maria-perez-cv",
                "organizacion": "Banco de Alimentos",
                "funcion": "Coordinadora digital",
                "impacto": "Digitalizacion del registro de entregas y voluntarios.",
                "fecha_inicio": datetime.strptime("2022-03-01", "%Y-%m-%d").date(),
                "fecha_fin": datetime.strptime("2023-12-20", "%Y-%m-%d").date(),
                "en_curso": False,
                "orden": 2,
            },
            {
                "cv": "maria-perez-cv",
                "organizacion": "Mujeres en STEAM",
                "funcion": "Facilitadora",
                "impacto": "Talleres de orientacion profesional para estudiantes.",
                "fecha_inicio": datetime.strptime("2021-05-10", "%Y-%m-%d").date(),
                "fecha_fin": None,
                "en_curso": True,
                "orden": 3,
            }
        ],
        "social_network": {
            "cv": "maria-perez-cv",
            "linkedin": "https://linkedin.com/in/mariaperez",
            "github": "https://github.com/mariaperez",
            "portfolio": "https://mariaperez.dev",
            "twitter": "https://x.com/mariaperez",
            "otras": "https://behance.net/mariaperez",
        },
        "interests": [
            {"cv": "maria-perez-cv", "nombre": "Cocinar", "orden": 1},
            {"cv": "maria-perez-cv", "nombre": "STEAM", "orden": 2},
        ],
        "other_info": {
            "cv": "maria-perez-cv",
            "disponibilidad_viajar": True,
            "teletrabajo": "Si",
            "expectativa_salarial": "32000-36000 EUR bruto/anual",
            "notas": "Disponible para entrevistas tecnicas en horario laboral.",
        },
    }

    ordered_keys = [
        "experiencias",
        "education",
        "complementary_training",
        "skills",
        "languages",
        "projects",
        "achievements",
        "volunteering",
        "interests",
    ]

    for key in ordered_keys:
        data[key] = sorted(data[key], key=lambda item: item.get("orden", 0))

    return data


def cv_view(request):
    cv = get_cv_data()
    context = {
        "cv": {
            "personal_info": cv["personal_info"],
            "professional_profile": cv["professional_profile"],
            "social_network": cv["social_network"],
        },
        "experiencias": cv["experiencias"],
        "educaciones": cv["education"],
        "formaciones": cv["complementary_training"],
        "habilidades": cv["skills"],
        "idiomas": cv["languages"],
        "proyectos": cv["projects"],
        "logros": cv["achievements"],
        "voluntariados": cv["volunteering"],
        "intereses": cv["interests"],
        "other_info": cv["other_info"],
    }
    return render(request, "cv/index.html", context)


def cv_json_view(request):
    return JsonResponse(get_cv_data())
