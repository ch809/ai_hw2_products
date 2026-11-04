
from fastapi import APIRouter
from ai_hw2_products.modules.home.router import router as home_router

api_router = APIRouter()
api_router.include_router(home_router)