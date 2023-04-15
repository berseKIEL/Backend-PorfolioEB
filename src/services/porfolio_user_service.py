from src.schemas.porfolio_schema import UserPorfolioSchemaIn
from src.models.porfolio_model import Porfolio
from src.core.security import get_password
from src.core.security import verify_password
from datetime import datetime
from typing import Optional
from uuid import UUID


class PorfolioUserService():
    @staticmethod
    async def create_user_porfolio(user: UserPorfolioSchemaIn):
        user_in = Porfolio(
            # Login
            email=user.email,
            username=user.username,
            password=get_password(user.password),
        )
        await user_in.save()
        return user_in

    @staticmethod
    async def authenticate(useroremail: str, password: str) -> Optional[Porfolio]:
        # Obtener usuario por email
        user = await PorfolioUserService.get_user_by_email(email=useroremail)
        if not user:
            # Obtener usuario por correo
            user = await PorfolioUserService.get_user_by_username(username=useroremail)
            if not user:
                return None

        if not verify_password(password=password, hashed_password=user.password):
            return None

        return user

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[Porfolio]:
        user = await Porfolio.find_one(Porfolio.email == email)
        return user

    @staticmethod
    async def get_user_by_username(username: str) -> Optional[Porfolio]:
        user = await Porfolio.find_one(Porfolio.username == username)
        return user

    @staticmethod
    async def get_user_by_id(id: UUID) -> Optional[Porfolio]:
        user = await Porfolio.find_one(Porfolio.porfolio_id == id)
        return user
