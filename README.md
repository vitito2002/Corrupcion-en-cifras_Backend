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
│   └── .env
└── frontend/         # Frontend (pendiente de implementación)
```

## Backend

El backend está desarrollado con FastAPI y se encuentra en la carpeta `backend/`.

Para más información sobre cómo ejecutar el backend, consulta el [README del backend](./backend/README.md).

### Endpoints Disponibles

- `GET /` - Verificación de estado
- `GET /analytics/casos-por-estado` - Casos por estado procesal
- `GET /analytics/jueces-mayor-demora` - Jueces con mayor demora promedio
- `GET /analytics/causas-iniciadas-por-ano` - Evolución temporal de causas
- `GET /analytics/delitos-mas-frecuentes` - Delitos más frecuentes
- `GET /analytics/causas-en-tramite-por-juzgado` - Causas en trámite por juzgado
- `GET /analytics/duracion-instruccion` - Duración de instrucción de causas

## Frontend

El frontend se implementará en la carpeta `frontend/`.

## Desarrollo

### Requisitos

- Python 3.11+
- PostgreSQL 15
- Docker y Docker Compose (opcional)

### Inicio Rápido

1. Navegar a la carpeta backend:
   ```bash
   cd backend
   ```

2. Configurar variables de entorno:
   ```bash
   cp .env.example .env
   # Editar .env con tus credenciales
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

