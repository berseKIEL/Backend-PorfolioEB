from beanie import Document, Indexed
from pydantic import Field, EmailStr
from uuid import UUID, uuid4
from typing import Dict, Optional
from datetime import datetime
from src.models.general_model import Translation


class User(Document):
    user_id: UUID = Field(default_factory=uuid4)
    # Login
    username: Indexed(str, unique=True)
    email: Indexed(EmailStr, unique=True)
    password: str

    # UserData
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    title: Translation = None
    phone: Optional[str] = None
    description: Translation = None
    country: Optional[str] = None
    province: Optional[str] = None

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<User {self.username}>"

    def __str__(self) -> str:
        return self.username

    def __hash__(self) -> int:
        return hash(self.username)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.username == other.username
        return False

    class Settings:
        name = 'users'
