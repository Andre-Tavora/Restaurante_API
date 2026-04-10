from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.database.connection import products_collection
from app.schemas.product_schema import ProductCreate
from app.models.product_model import product_helper

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/")
def create_product(product: ProductCreate):
    result = products_collection.insert_one(product.dict())
    return {
        "id": str(result.inserted_id),
        "message": "Product created"
    }


@router.get("/")
def get_products():
    return [product_helper(product) for product in products_collection.find()]


@router.get("/{product_id}")
def get_product_by_id(product_id: str):
    product = products_collection.find_one({"_id": ObjectId(product_id)})

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product_helper(product)


@router.put("/{product_id}")
def update_product(product_id: str, product: ProductCreate):
    result = products_collection.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": product.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    updated_product = products_collection.find_one({"_id": ObjectId(product_id)})
    return {
        "message": "Product updated",
        "product": product_helper(updated_product)
    }


@router.delete("/{product_id}")
def delete_product(product_id: str):
    result = products_collection.delete_one({"_id": ObjectId(product_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    return {"message": "Product deleted"}