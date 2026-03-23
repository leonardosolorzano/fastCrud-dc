# 🐦 TwitterClone API — FastAPI

API REST tipo Twitter/X construida con FastAPI, SQLAlchemy async, PostgreSQL y Redis.
Soporta entornos `dev`, `staging` y `production` con configuración por variables de entorno.

---

## Stack tecnológico

| Capa | Tecnología |
|------|-----------|
| Framework | FastAPI 0.111+ |
| ORM | SQLAlchemy 2.0 async |
| Base de datos | PostgreSQL (prod) / SQLite (dev) |
| Caché / Rate-limit | Redis |
| Migraciones | Alembic |
| Auth | JWT (python-jose) + bcrypt |
| Validación | Pydantic v2 |
| Testing | pytest + httpx |
| Contenedores | Docker + Docker Compose |

---

## Estructura de carpetas

```
twitter_clone/
│
├── app/                          # Código fuente principal
│   ├── __init__.py
│   ├── main.py                   # Entrada FastAPI, registro de routers y middleware
│   │
│   ├── core/                     # Configuración y utilidades transversales
│   │   ├── __init__.py
│   │   ├── config.py             # Settings por entorno (Pydantic BaseSettings)
│   │   ├── security.py           # JWT, hashing de contraseñas
│   │   ├── dependencies.py       # Inyección de dependencias (DB session, usuario actual)
│   │   └── exceptions.py         # Manejadores de error globales
│   │
│   ├── db/                       # Capa de base de datos
│   │   ├── __init__.py
│   │   ├── base.py               # Base declarativa SQLAlchemy
│   │   ├── session.py            # Motor async y SessionLocal
│   │   └── redis.py              # Cliente Redis
│   │
│   ├── models/                   # Modelos ORM (tablas)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── post.py
│   │   └── like.py
│   │
│   ├── schemas/                  # Schemas Pydantic (request / response)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── post.py
│   │   └── token.py
│   │
│   ├── repositories/             # Acceso a datos (sin lógica de negocio)
│   │   ├── __init__.py
│   │   ├── base.py               # CRUD genérico
│   │   ├── user_repository.py
│   │   └── post_repository.py
│   │
│   ├── services/                 # Lógica de negocio
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── post_service.py
│   │   └── user_service.py
│   │
│   └── routers/                  # Endpoints HTTP
│       ├── __init__.py
│       ├── auth.py
│       ├── posts.py
│       └── users.py
│
├── migrations/                   # Alembic
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│
├── tests/                        # Suite de pruebas
│   ├── __init__.py
│   ├── conftest.py               # Fixtures compartidos
│   ├── test_auth.py
│   ├── test_posts.py
│   └── test_users.py
│
├── .env.dev                      # Variables de entorno desarrollo
├── .env.staging                  # Variables staging
├── .env.production               # Variables producción (NO subir a git)
├── .env.example                  # Plantilla pública
├── .gitignore
├── alembic.ini
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── Dockerfile
├── pyproject.toml                # Dependencias y configuración
└── README.md
```

---

## Configuración de entornos

### Desarrollo local
```bash
cp .env.example .env.dev
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
APP_ENV=dev uvicorn app.main:app --reload
```

### Docker (staging)
```bash
docker compose -f docker-compose.dev.yml up --build
```

### Producción
```bash
APP_ENV=production docker compose -f docker-compose.prod.yml up -d
```

---

## Migraciones
```bash
# Crear migración
alembic revision --autogenerate -m "add posts table"

# Aplicar
alembic upgrade head

# Revertir
alembic downgrade -1
```

---

## Pruebas
```bash
pytest                            # Todas las pruebas
pytest -v --cov=app               # Con cobertura
pytest tests/test_posts.py -k "test_create"  # Filtro
```

---

## Documentación interactiva
- Swagger UI: http://localhost:8000/docs
- ReDoc:       http://localhost:8000/redoc
- OpenAPI JSON: http://localhost:8000/openapi.json