from fastapi import APIRouter

router = APIRouter()

produtos = []

@router.get("/produtos")
def listar_produtos():
    return produtos

@router.post("/produtos")
def criar_produto(produto: dict):
    produtos.append(produto)
    return produto