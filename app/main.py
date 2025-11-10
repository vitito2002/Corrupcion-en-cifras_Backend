from fastapi import FastAPI

app = FastAPI(title="Corrupción en Cifras API")


@app.get("/")
def read_root():
    return {"message": "API funcionando ✅"}

