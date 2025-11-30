# Corrupción en Cifras - Backend

Backend FastAPI para el dashboard de visualizaciones "Corrupción en Cifras".

## Descripción

API REST desarrollada con FastAPI que proporciona endpoints para consultar y analizar datos de casos de corrupción en Argentina. La arquitectura sigue un patrón de capas con repositories, services y routers.

## Requisitos

- Python 3.11+
- PostgreSQL 15
- Docker y Docker Compose (opcional)

## Instalación

### Opción 1: Con Docker Compose (Recomendado)

```bash
docker compose up
```

La API estará disponible en `http://localhost:8000`

### Opción 2: Desarrollo Local

1. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno:
   - Copiar `.env.example` a `.env`
   - Ajustar `DATABASE_URL` para usar `localhost` en lugar de `db` si corres PostgreSQL localmente

4. Ejecutar la aplicación:
```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000`

## Estructura del Proyecto

```
app/
├── main.py              # Punto de entrada FastAPI
├── core/                # Configuración y base de datos
├── models/              # Modelos SQLAlchemy
├── repositories/        # Acceso a datos
├── services/            # Lógica de negocio
├── routers/             # Endpoints
├── schemas/             # Schemas Pydantic
└── utils/               # Utilidades
```

## Variables de Entorno

Ver `.env.example` para la lista completa de variables requeridas.

## Endpoints

- `GET /` - Health check
- `GET /analytics/casos-por-estado` - Casos por estado procesal
- `GET /analytics/jueces-mayor-demora` - Jueces con mayor demora promedio
- `GET /analytics/causas-iniciadas-por-ano` - Evolución temporal de causas
- `GET /analytics/delitos-mas-frecuentes` - Delitos más frecuentes
- `GET /analytics/causas-en-tramite-por-juzgado` - Causas en trámite por juzgado
- `GET /analytics/duracion-instruccion` - Duración de instrucción de causas
- `GET /analytics/causas-por-fuero` - Causas por fuero judicial
- `GET /analytics/causas-por-fiscal` - Causas por fiscal
- `GET /analytics/personas-mas-denunciadas` - Personas más denunciadas
- `GET /analytics/personas-que-mas-denunciaron` - Personas que más denunciaron
- `GET /exportacion/descargar-base-de-datos` - Descargar base de datos completa

Documentación interactiva disponible en `http://localhost:8000/docs`