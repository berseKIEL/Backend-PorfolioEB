from src.schemas.porfolio_schema import UserPorfolioSchemaIn
from src.models.porfolio_model import Porfolio
from src.core.security import get_password
from src.core.security import verify_password
from datetime import datetime
from typing import Optional


class PorfolioUserService():
    @staticmethod
    async def create_user_porfolio(user: UserPorfolioSchemaIn):
        user_in = Porfolio(
            # Login
            email=user.email,
            username=user.username,
            password=get_password(user.password),

            # Creation
            date_creation=datetime.utcnow(),
            date_modified=datetime.utcnow()
        )
        await user_in.save()
        return user_in

    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[Porfolio]:
        user = await PorfolioUserService.get_user_by_email(email=email)
        if not user:
            return None
        if not verify_password(password=password, hashed_password=user.password):
            return None
        return user

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[Porfolio]:
        user = await Porfolio.find_one(Porfolio.email == email)
        return user
