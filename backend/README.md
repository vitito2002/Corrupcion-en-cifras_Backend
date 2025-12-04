# Corrupción en Cifras - Backend

Backend FastAPI para el dashboard de visualizaciones "Corrupción en Cifras".

## Descripción

API REST desarrollada con FastAPI que proporciona endpoints para consultar y analizar datos de casos de corrupción en Argentina. La arquitectura sigue un patrón de capas con repositories, services y routers.

## Requisitos

- Docker 20.10+
- Docker Compose 2.0+

**Nota:** No es necesario tener Python o PostgreSQL instalados localmente. Todo se ejecuta dentro de contenedores Docker.

## Instalación y Ejecución con Docker

### Opción A: Backend Standalone (con su propia base de datos)

Esta opción crea una instancia completa del backend con su propia base de datos PostgreSQL.

#### 1. Configurar Variables de Entorno

Copia el archivo de ejemplo y ajusta los valores:

```bash
cp .env.example .env
```

Edita el archivo `.env` con los valores por defecto (que coinciden con la pipeline):

```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=td8corrupcion
POSTGRES_DB=corrupcion_db
POSTGRES_PORT=5433
API_PORT=8000
DATABASE_URL=postgresql://admin:td8corrupcion@db:5432/corrupcion_db
```

**Importante:** El `DATABASE_URL` debe usar `db` como hostname (nombre del servicio de PostgreSQL en docker-compose).

#### 2. Levantar los Contenedores

```bash
docker compose up --build
```

Este comando:
- Construye la imagen de la API
- Descarga la imagen de PostgreSQL 15-alpine
- Crea y levanta ambos contenedores
- Configura la red entre contenedores
- Espera a que la base de datos esté lista antes de iniciar la API

### Opción B: Conectarse a la Base de Datos de la Pipeline

Si ya tienes la pipeline corriendo con su propia base de datos, puedes hacer que el backend se conecte a esa base de datos existente.

#### 1. Configurar Variables de Entorno

Copia el archivo de ejemplo:

```bash
cp .env.example .env
```

Edita el archivo `.env` para conectarte al servicio `postgres` de la pipeline:

```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=td8corrupcion
POSTGRES_DB=corrupcion_db
API_PORT=8000
DATABASE_URL=postgresql://admin:td8corrupcion@postgres:5432/corrupcion_db
```

**Importante:** 
- El `DATABASE_URL` debe usar `postgres` como hostname (nombre del servicio en el docker-compose de la pipeline)
- Asegúrate de que la pipeline esté corriendo antes de levantar el backend

#### 2. Modificar docker-compose.yaml

Edita `docker-compose.yaml` y:

1. **Comenta el servicio `db`** (no necesitas crear otra base de datos)
2. **Descomenta la red externa** en la sección `networks`:
   ```yaml
   networks:
     backend_network:
       driver: bridge
     corrupcion_network:
       external: true
   ```
3. **Agrega la red `corrupcion_network` al servicio `api`**:
   ```yaml
   api:
     networks:
       - backend_network
       - corrupcion_network
   ```
4. **Elimina el `depends_on` del servicio `api`** (ya no depende de `db`)

#### 3. Levantar solo el servicio API

```bash
docker compose up api --build
```

O si prefieres, puedes crear un `docker-compose.override.yaml` para esta configuración.

### 3. Acceder a la API (Ambas Opciones)

Una vez que los contenedores estén corriendo, la API estará disponible en:

- **API Base:** `http://localhost:8000`
- **Documentación Swagger:** `http://localhost:8000/docs`
- **Documentación ReDoc:** `http://localhost:8000/redoc`
- **Health Check:** `http://localhost:8000/`

### 4. Detener los Contenedores

Para detener los contenedores:

```bash
docker compose down
```

Para detener y eliminar los volúmenes (incluyendo los datos de la base de datos):

```bash
docker compose down -v
```

### 5. Ver Logs

Para ver los logs de los contenedores:

```bash
# Todos los servicios
docker compose logs

# Solo la API
docker compose logs api

# Solo la base de datos
docker compose logs db

# Seguir logs en tiempo real
docker compose logs -f
```

## Desarrollo Local (Opcional)

Si prefieres ejecutar el proyecto sin Docker:

1. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno:
   - Copiar `.env.example` a `.env`
   - Cambiar `DATABASE_URL` para usar `localhost` en lugar de `db`

4. Ejecutar la aplicación:
```bash
uvicorn app.main:app --reload
```

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