# 🧪 Guía de Verificación del Proyecto

## ✅ Checklist de Verificación

### 1. Verificar archivos de configuración

```bash
# Verificar que existen los archivos necesarios
ls -la .env .env.example docker-compose.yaml Dockerfile requirements.txt
```

### 2. Verificar variables de entorno

```bash
# Verificar que .env tiene DATABASE_URL
grep DATABASE_URL .env
```

### 3. Instalar dependencias (Desarrollo Local)

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### 4. Ejecutar script de verificación

```bash
python test_setup.py
```

Este script verifica:
- ✅ Que todas las importaciones funcionan
- ✅ Que la configuración se carga correctamente
- ✅ Que FastAPI está configurado

### 5. Probar la aplicación (Desarrollo Local)

```bash
# Ejecutar el servidor
uvicorn app.main:app --reload
```

**Verificar:**
- ✅ El servidor arranca sin errores
- ✅ Abrir en el navegador: http://localhost:8000
- ✅ Debe mostrar: `{"message": "API funcionando ✅"}`
- ✅ Abrir: http://localhost:8000/docs
- ✅ Debe mostrar la documentación interactiva de FastAPI

### 6. Probar con Docker Compose

```bash
# Levantar los servicios
docker compose up

# En otra terminal, verificar que los contenedores están corriendo
docker ps
```

**Verificar:**
- ✅ Contenedor `corrupcion_api` está corriendo
- ✅ Contenedor `corrupcion_db` está corriendo
- ✅ Abrir: http://localhost:8000
- ✅ Debe mostrar: `{"message": "API funcionando ✅"}`
- ✅ Abrir: http://localhost:8000/docs

### 7. Verificar conexión a base de datos (Opcional)

```bash
# Conectar a PostgreSQL desde Docker
docker exec -it corrupcion_db psql -U postgres -d corrupcion_db

# Dentro de psql, ejecutar:
\dt  # Listar tablas (debería estar vacío por ahora)
\q   # Salir
```

## 🐛 Problemas Comunes

### Error: "ModuleNotFoundError: No module named 'fastapi'"
**Solución:** Instalar dependencias: `pip install -r requirements.txt`

### Error: "ValidationError" al cargar Settings
**Solución:** Verificar que `.env` existe y tiene `DATABASE_URL`

### Error: "Connection refused" en Docker
**Solución:** Verificar que `docker compose up` está corriendo

### Error: "Port 8000 already in use"
**Solución:** Cambiar el puerto en `docker-compose.yaml` o detener el proceso que usa el puerto

## 📊 Resultado Esperado

Si todo funciona correctamente:

1. ✅ `python test_setup.py` muestra todas las verificaciones en verde
2. ✅ `uvicorn app.main:app --reload` arranca sin errores
3. ✅ http://localhost:8000 devuelve `{"message": "API funcionando ✅"}`
4. ✅ http://localhost:8000/docs muestra la documentación de FastAPI
5. ✅ `docker compose up` levanta ambos servicios sin errores

