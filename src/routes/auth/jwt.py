from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from src.services.porfolio_user_service import PorfolioUserService
from src.core.security import create_access_token, create_refresh_token

auth_router = APIRouter()

@auth_router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends())-> Any:
    user = await PorfolioUserService.authenticate(useroremail=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Las credenciales son invalidas"
        )
        
    # Crear accesos y refresh token
    return {
        "access_token": create_access_token(user.porfolio_id),
        "refresh_token": create_refresh_token(user.porfolio_id)
    }