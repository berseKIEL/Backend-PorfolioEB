from fastapi import APIRouter
from src.routes.handlers import user_handler
from src.routes.auth.jwt import auth_router

router = APIRouter()

router.include_router(user_handler.user_router, prefix='/user', tags=['user'])

router.include_router(auth_router, prefix='/auth', tags=["auth"])
