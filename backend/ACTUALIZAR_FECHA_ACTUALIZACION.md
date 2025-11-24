# Cómo actualizar la fecha de última actualización desde el Scrapper

## Opción 1: Usando el Repository de Python (Recomendado)

Si tu scrapper está en Python y tiene acceso a la base de datos, puedes usar el repository directamente:

```python
from app.repositories.metadata_repository import MetadataRepository
from app.core.database import SessionLocal
from datetime import datetime

# Al finalizar la actualización de datos
db = SessionLocal()
try:
    metadata_repo = MetadataRepository(db)
    metadata_repo.actualizar_fecha_actualizacion(datetime.now())
finally:
    db.close()
```

## Opción 2: Usando SQL directo

Si prefieres actualizar directamente desde SQL al finalizar el scrapper:

```sql
-- Actualizar la fecha de última actualización
INSERT INTO metadata (clave, valor)
VALUES ('ultima_actualizacion', NOW())
ON CONFLICT (clave) 
DO UPDATE SET valor = NOW();
```

## Opción 3: Usando el endpoint (si el scrapper puede hacer HTTP requests)

```bash
# El endpoint actualmente solo lee, pero podrías crear uno de escritura si es necesario
# Por ahora, usa las opciones 1 o 2
```

## Notas

- La tabla `metadata` se crea automáticamente si usas SQLAlchemy con `Base.metadata.create_all()`
- O puedes ejecutar el script `scripts/create_metadata_table.sql` manualmente
- El sistema tiene un fallback: si no existe la fecha en metadata, usa la fecha más reciente de `fecha_ultimo_movimiento` de los expedientes

