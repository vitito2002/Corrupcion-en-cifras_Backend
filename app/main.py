from fastapi import FastAPI
from app.routers import analytics_router

app = FastAPI(title="Corrupción en Cifras API")

# Registrar routers
app.include_router(analytics_router.router)


@app.get("/")
def read_root():
    return {"message": "API funcionando ✅"}

