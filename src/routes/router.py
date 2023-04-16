from fastapi import APIRouter
from src.routes.handlers import user_handler, skill_handler, project_handler, porfolio_handler
from src.routes.auth.jwt import auth_router

router = APIRouter()

# Router para modelos
router.include_router(user_handler.user_router, prefix='/user', tags=['Users'])
router.include_router(skill_handler.skill_router, prefix='/skill', tags=['Skills'])
router.include_router(project_handler.project_handler, prefix='/project', tags=['Projects'])
router.include_router(porfolio_handler.porfolio_router, prefix='/porfolio', tags=['Porfolios'])

# router para el auth de JWT
router.include_router(auth_router, prefix='/auth', tags=["Auth"])