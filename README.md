# Corrupción en Cifras

Dashboard de visualizaciones sobre casos de corrupción en Argentina.

## Estructura del Proyecto

```
.
├── backend/          # Backend FastAPI
│   ├── app/          # Aplicación FastAPI
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── docker-compose.yaml
│   └── scripts/      # Scripts ETL y utilidades
└── frontend/         # Frontend React + TypeScript
    ├── src/          # Código fuente
    └── package.json
```

## Requisitos

- Python 3.11+
- Node.js 18+
- PostgreSQL 15
- Docker y Docker Compose (opcional)

## Inicio Rápido

### Backend

Para más información sobre cómo ejecutar el backend, consulta el [README del backend](./backend/README.md).

1. Navegar a la carpeta backend:
   ```bash
   cd backend
   ```

2. Configurar variables de entorno:
   ```bash
   cp .env.example .env
   ```

3. Ejecutar con Docker Compose:
   ```bash
   docker compose up
   ```

4. O ejecutar localmente:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

La API estará disponible en `http://localhost:8000`
Documentación interactiva en `http://localhost:8000/docs`

### Frontend

Para más información sobre cómo ejecutar el frontend, consulta el [README del frontend](./frontend/README.md).

1. Navegar a la carpeta frontend:
   ```bash
   cd frontend
   ```

2. Instalar dependencias:
   ```bash
   npm install
   ```

3. Ejecutar en desarrollo:
   ```bash
   npm run dev
   ```

La aplicación estará disponible en `http://localhost:5173`

## Endpoints Principales

- `GET /` - Verificación de estado
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

