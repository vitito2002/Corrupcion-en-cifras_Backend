from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import (
    expedientes_por_estado_procesal_router,
    jueces_mayor_demora_router,
    causas_iniciadas_por_ano_router,
    delitos_mas_frecuentes_router,
    causas_en_tramite_por_juzgado_router,
    duracion_instruccion_router,
    duracion_outliers_router,
    exportacion_router,
    causas_por_fuero_router,
    personas_mas_denunciadas_router,
    personas_que_mas_denunciaron_router,
    causas_por_fiscal_router
)

app = FastAPI(title="Corrupción en Cifras API")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",
        "http://localhost:5173",  # Por si cambias el puerto de Vite
        "http://127.0.0.1:5174",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los headers
)

# Registrar routers
app.include_router(expedientes_por_estado_procesal_router.router)
app.include_router(jueces_mayor_demora_router.router)
app.include_router(causas_iniciadas_por_ano_router.router)
app.include_router(delitos_mas_frecuentes_router.router)
app.include_router(causas_en_tramite_por_juzgado_router.router)
app.include_router(duracion_instruccion_router.router)
app.include_router(duracion_outliers_router.router)
app.include_router(exportacion_router.router)
app.include_router(causas_por_fuero_router.router)
app.include_router(personas_mas_denunciadas_router.router)
app.include_router(personas_que_mas_denunciaron_router.router)
app.include_router(causas_por_fiscal_router.router)


@app.get("/")
def read_root():
    return {"message": "API funcionando ✅"}

