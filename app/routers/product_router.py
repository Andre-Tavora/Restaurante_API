from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.models.products import Product
from app.schemas.product_schema import ProductCreate, ProductResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/produtos", response_model=list[ProductResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.post("/produtos", response_model=ProductResponse)
def criar_produto(produto: ProductCreate, db: Session = Depends(get_db)):
    novo_produto = Product(nome=produto.nome, preco=produto.preco)
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto