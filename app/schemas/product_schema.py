from pydantic import BaseModel

class ProductCreate(BaseModel):
    nome: str
    preco: float

class ProductResponse(BaseModel):
    id: int
    nome: str
    preco: float

    class Config:
        from_attributes = True