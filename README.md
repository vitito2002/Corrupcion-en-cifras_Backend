# Corrupción en Cifras - Backend

Backend FastAPI para el dashboard de visualizaciones "Corrupción en Cifras".

## 🚀 Inicio Rápido

### Opción 1: Con Docker Compose (Recomendado)

```bash
docker compose up
```

La API estará disponible en `http://localhost:8000`

### Opción 2: Desarrollo Local (sin Docker)

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
   - Ajustar `DATABASE_URL` para usar `localhost` en lugar de `db` si corres PostgreSQL localmente

4. Ejecutar la aplicación:
```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000`

## 📁 Estructura del Proyecto

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

## 🔧 Variables de Entorno

Ver `.env.example` para la lista completa de variables requeridas.

## 📝 Endpoints

- `GET /` - Health check: `{"message": "API funcionando ✅"}`