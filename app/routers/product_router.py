from fastapi import APIRouter, Depends, HTTPException
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

@router.put("/produtos/{produto_id}", response_model=ProductResponse)
def atualizar_produto(produto_id: int, produto: ProductCreate, db: Session = Depends(get_db)):
    produto_db = db.query(Product).filter(Product.id == produto_id).first()

    if not produto_db:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    produto_db.nome = produto.nome
    produto_db.preco = produto.preco

    db.commit()
    db.refresh(produto_db)

    return produto_db

@router.delete("/produtos/{produto_id}")
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Product).filter(Product.id == produto_id).first()

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    db.delete(produto)
    db.commit()

    return {"mensagem": "Produto removido com sucesso"}