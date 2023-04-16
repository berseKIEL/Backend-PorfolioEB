from fastapi import APIRouter
from src.routes.handlers import user_handler, skill_handler
from src.routes.auth.jwt import auth_router

router = APIRouter()

# router para el auth de JWT
router.include_router(auth_router, prefix='/auth', tags=["auth"])


# Router para modelos
router.include_router(user_handler.user_router, prefix='/user', tags=['user'])
router.include_router(skill_handler.skill_router, prefix='/skill', tags=['skills'])