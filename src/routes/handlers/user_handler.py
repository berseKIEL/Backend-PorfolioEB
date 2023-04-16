from fastapi import APIRouter, HTTPException, status
from src.schemas.user_schema import UserSchemaIn, UserSchemaOut
from src.services.user_service import UserService
import pymongo

user_router = APIRouter()


@user_router.post('/create', summary="Crear un nuevo usuario.", response_model=UserSchemaOut)
async def create_user(data: UserSchemaIn):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Un usuario con esas credenciales ya existe."
        )