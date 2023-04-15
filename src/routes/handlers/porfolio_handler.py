from fastapi import APIRouter, HTTPException, status
from src.schemas.porfolio_schema import UserPorfolioSchemaIn, UserPorfolioSchemaOut, PorfolioSchema
from src.services.porfolio_user_service import PorfolioUserService
from src.services.porfolio_service import PorfolioService
import pymongo
from typing import List

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


@porfolio_router.get('/get', summary="Obtiene toda la información relevante de todos los porfolios", response_model=List[PorfolioSchema])
async def get_all_porfolio():
    return await PorfolioService.get_all_porfolio()


@porfolio_router.get('/get/id', summary="Obtiene la información de un solo porfolio especificado de un usuario", response_model=PorfolioSchema)
async def get_porfolio():
    return await PorfolioService.get_porfolio()
