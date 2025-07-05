# Task API 📝

API REST para gestionar tareas, desarrollada con FastAPI, PostgreSQL y SQLAlchemy.

---

## 🚀 Cómo levantar el proyecto localmente

### 1. Instalar dependencias

```bash
poetry install

.\runserver.bat

La aplicación estará disponible en: http://127.0.0.1:8000

GET /api/v1/health → Verifica que la API esté activa

Documentación Swagger:
http://127.0.0.1:8000/docs

🛠️ Stack técnico
Python 3.12

FastAPI

Uvicorn

SQLAlchemy

Poetry

📂 Estructura inicial

app/
├── main.py
└── api/
    └── v1/
        └── endpoints/
            └── health.py
```
