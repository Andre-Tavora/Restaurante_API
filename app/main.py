from fastapi import FastAPI
from app.routers import product_router

app = FastAPI(title="Restaurant API")

app.include_router(product_router.router)