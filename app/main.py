from fastapi import FastAPI
from app.routers.product_router import router

app = FastAPI(
    title="Restaurante API",
    description="API de restaurante com FastAPI e MongoDB",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Restaurante API rodando"}