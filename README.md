# Task API 📝

API REST para gestionar tareas, desarrollada con **FastAPI**, **PostgreSQL** y **SQLAlchemy**.

---

## 🚀 Levantar el proyecto localmente

### 1. Instalar dependencias

```
poetry install
```

### 2. Ejecutar el servidor

```
.\runserver.bat
```

La app estará disponible en **http://127.0.0.1:8000**

---

## 🔍 Endpoints principales

| Método | Ruta             | Descripción                     |
| ------ | ---------------- | ------------------------------- |
| GET    | `/api/v1/health` | Verifica que la API esté activa |

Documentación Swagger: **http://127.0.0.1:8000/docs**

---

## 🛠️ Stack técnico

- Python 3.12
- FastAPI + Uvicorn
- SQLAlchemy
- Poetry

---

## 📂 Estructura inicial

```
app/
├─ main.py
└─ api/
   └─ v1/
      └─ endpoints/
         └─ health.py
```

---

## 🗘️ Roadmap

- ✅ Sprint 0: Bootstrap y health-check
- ⏳ Sprint 1: Autenticación de usuarios
- ⏳ Sprint 2: CRUD de tareas
- ⏳ Sprint 3: Deploy & CI/CD

---

## 📝 Licencia

MIT
