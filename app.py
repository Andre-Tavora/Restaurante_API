from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Restaurant API")

produtos = []

class Produto(BaseModel):
    id: int
    nome: str
    preco: float

@app.get("/")
def home():
    return {"mensagem": "API do restaurante no ar"}

@app.get("/produtos", response_model=List[Produto])
def listar_produtos():
    return produtos

@app.post("/produtos", response_model=Produto)
def criar_produto(produto: Produto):
    produtos.append(produto)
    return produto