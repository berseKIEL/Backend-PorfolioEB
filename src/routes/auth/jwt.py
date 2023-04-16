from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from src.services.user_service import UserService
from src.core.security import create_access_token, create_refresh_token
from src.schemas.auth_schema import TokenSchema
from src.schemas.user_schema import UserSchemaOut
from src.schemas.auth_schema import TokenPayload
from src.models.user_model import User
from src.routes.deps.user_deps import get_current_user
from src.core.config import settings
from jose import jwt
from pydantic import ValidationError

auth_router = APIRouter()


@auth_router.post('/login', summary="Crea el acceso de la ruta para los usuarios", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UserService.authenticate(useroremail=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Las credenciales son invalidas"
        )

    # Crear accesos y refresh token
    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id)
    }


@auth_router.post('/check_token', summary="Prueba si el Token es valido", response_model=UserSchemaOut)
async def check_token(user: User = Depends(get_current_user)) -> str:
    return user


@auth_router.post('/refresh', summary="Refrezca el JWT token", response_model=TokenSchema)
async def refresh_token(refresh_token: str = Body(...)):
    try:
        payload = jwt.decode(
            token=refresh_token,
            key=settings.JWT_REFRESH_SECRET_KEY,
            algorithms=[settings.ALGORITH]
        )

        token_data = TokenPayload(**payload)

    except (jwt.JWTError, ValidationError) as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No se pudo validar el token",
            headers={"WWW-Authenticate": "Bearer"}
        )

    user = await UserService.get_user_by_id(token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se pudo encontrar el usuario",
        )

    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id)
    }
