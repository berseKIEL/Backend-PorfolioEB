from fastapi import APIRouter
from src.routes.handlers import porfolio_handler
from src.routes.auth.jwt import auth_router

router = APIRouter()

router.include_router(porfolio_handler.porfolio_router,
                      prefix='/porfolio', tags=['porfolio'])

router.include_router(auth_router, prefix='/auth', tags=["auth"])
