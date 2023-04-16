from fastapi import APIRouter, HTTPException, status, Depends
from src.schemas.user_schema import UserSchemaIn, UserSchemaOut, UserUpdate
from src.services.user_service import UserService
from src.models.user_model import User
from src.routes.deps.user_deps import get_current_user
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


@user_router.put('/update', summary="Actualiza la información y los datos de un usuario", response_model=UserSchemaOut)
async def update_user(data: UserUpdate, current_user: User = Depends(get_current_user)):
    try:
        return await UserService.update_user(current_user, data)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontro el usuario"
        )
