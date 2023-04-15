from fastapi import Depends, HTTPException, status
from pydantic import ValidationError
from fastapi.security import OAuth2PasswordBearer
from src.core.config import settings
from src.models.porfolio_model import Porfolio
from jose import jwt
from src.schemas.auth_schema import TokenPayload
from datetime import datetime
from src.services.porfolio_user_service import PorfolioUserService

oauth_jwt = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_ROUTE}/auth/login",
    scheme_name="JWT"
)


async def get_current_user(token: str = Depends(oauth_jwt)) -> Porfolio:
    try:
        payload = jwt.decode(
            token= token, 
            key= settings.JWT_SECRET_KEY,
            algorithms=[settings.ALGORITH]
        )
                
        token_data = TokenPayload(**payload)
        

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Session expirada, inicia sesión de nuevo",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
    except (jwt.JWTError, ValidationError) as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No se pudo validar el token",
            headers={"WWW-Authenticate": "Bearer"}
        )

    user = await PorfolioUserService.get_user_by_id(token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se pudo encontrar el usuario",
        )

    return user
