
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ai_hw2_products.core.config import get_settings

router = APIRouter(tags=["Products"])


settings = get_settings()



class ProductSetting(BaseModel):
    id : int
    name : str
    price :int
    stock : int
    
    
products = [
{"id": 1, "name": "Mouse", "price": 590, "stock": 10},
{"id": 2, "name": "Keyboard", "price": 1290, "stock": 5},
{"id": 3, "name": "Monitor", "price": 4990, "stock": 2},
]


# http://localhost:8000/api/v1/products
@router.get("/products")
def get_products():
    return products

@router.get("/products/{product_id}")
def get_product_info(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(status_code=404, detail="Product not found")

@router.post("/products",status_code = 201)
def post_products(product : ProductSetting):
    products.append(product)
    return {"status": "success"}