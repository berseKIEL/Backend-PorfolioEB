from fastapi import APIRouter, HTTPException, status
from src.schemas.porfolio_schema import UserPorfolioSchemaIn, UserPorfolioSchemaOut
from src.services.porfolio_user_service import PorfolioUserService
import pymongo

porfolio_router = APIRouter()


@porfolio_router.post('/create', summary="Crear un nuevo porfolio", response_model=UserPorfolioSchemaOut)
async def create_porfolio(data: UserPorfolioSchemaIn):
    try:
        return await PorfolioUserService.create_user_porfolio(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Un usuario con esas credenciales ya existe."
        )