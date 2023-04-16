from fastapi import HTTPException, status
from src.schemas.user_schema import UserSchemaIn, UserUpdate
from src.models.user_model import User
from src.core.security import get_password
from src.core.security import verify_password
from typing import Optional, Union
from uuid import UUID


class UserService():
    @staticmethod
    async def create_user(user: UserSchemaIn):
        user_in = User(
            # Login
            email=user.email,
            username=user.username,
            password=get_password(user.password),
        )
        await user_in.save()
        return user_in

    @staticmethod
    async def authenticate(useroremail: str, password: str) -> Optional[User]:
        # Obtener usuario por email
        user = await UserService.get_user_by_email(email=useroremail)
        if not user:
            # Obtener usuario por correo
            user = await UserService.get_user_by_username(username=useroremail)
            if not user:
                return None

        if not verify_password(password=password, hashed_password=user.password):
            return None

        return user

    @staticmethod
    async def get_user(user: Union[str, User]) -> Optional[User]:
        if isinstance(user, str):
            try:
                # obtiene usuario por username
                user = await UserService.get_user_by_username(username=user)
                if user:
                    return user
            except:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No se encontro el usuario"
                )

            try:
                # obtiene usuario por correo
                user = await UserService.get_user_by_email(email=user)
                if user:
                    return user
            except:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No se encontro el usuario"
                )

            return None
        elif isinstance(user, User):
            try:
                # obtiene usuario por correo
                user = await UserService.get_user_by_email(email=user.email)
                if user:
                    return user
            except:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No se encontro el usuario"
                )

            try:
                # obtiene usuario por username
                user = await UserService.get_user_by_username(username=user.username)
                if user:
                    return user
            except:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No se encontro el usuario"
                )

            return None
        else:
             raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No se encontro el usuario"
                )

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        user = await User.find_one(User.email == email)
        return user

    @staticmethod
    async def get_user_by_username(username: str) -> Optional[User]:
        user = await User.find_one(User.username == username)
        return user

    @staticmethod
    async def get_user_by_id(id: UUID) -> Optional[User]:
        user = await User.find_one(User.user_id == id)
        return user

    @staticmethod
    async def update_user(user: User, data: UserUpdate):
        user = await UserService.get_user(user)
        await user.update({"$set": data.dict(exclude_unset=True)})
        await user.save()
        return user
