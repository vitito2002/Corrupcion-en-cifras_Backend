from fastapi import FastAPI
from app.routers import expedientes_por_estado_procesal_router, jueces_mayor_demora_router

app = FastAPI(title="Corrupción en Cifras API")

# Registrar routers
app.include_router(expedientes_por_estado_procesal_router.router)
app.include_router(jueces_mayor_demora_router.router)


@app.get("/")
def read_root():
    return {"message": "API funcionando ✅"}

