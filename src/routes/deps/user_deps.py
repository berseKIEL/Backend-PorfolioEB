from fastapi import Depends, HTTPException, status
from pydantic import ValidationError
from jose import ExpiredSignatureError
from fastapi.security import OAuth2PasswordBearer
from src.core.config import settings
from src.models.user_model import User
from jose import jwt
from src.schemas.auth_schema import TokenPayload
from src.services.user_service import UserService

oauth_jwt = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_ROUTE}/auth/login",
    scheme_name="JWT"
)

async def get_current_user(token: str = Depends(oauth_jwt)) -> User:
    try:
        payload = jwt.decode(
            token=token,
            key=settings.JWT_SECRET_KEY,
            algorithms=[settings.ALGORITH]
        )

        token_data = TokenPayload(**payload)

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sesion expirada, inicia sesión de nuevo",
            headers={"WWW-Authenticate": "Bearer"},
        )

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

    return user
