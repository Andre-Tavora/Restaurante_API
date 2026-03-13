from sqlalchemy import Column, Integer, String, Float
from app.database.connection import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    preco = Column(Float, nullable=False)