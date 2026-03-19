from fastapi import FastAPI
from app.database.connection import engine, Base
from app.models.products import Product
from app.routers import product_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Restaurant API")

app.include_router(product_router.router)   