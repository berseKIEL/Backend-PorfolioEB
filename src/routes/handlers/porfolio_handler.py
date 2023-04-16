from fastapi import APIRouter
from src.schemas.porfolio_schema import PorfolioSchemaOut
from src.services.porfolio_service import PorfolioService

porfolio_router = APIRouter()


@porfolio_router.get('/{username}', summary="Obtiene toda la información relevante de tipo porfolio de un usuario", response_model=PorfolioSchemaOut)
async def get_porfolio(username: str):
    return await PorfolioService.get_porfolio(username)
