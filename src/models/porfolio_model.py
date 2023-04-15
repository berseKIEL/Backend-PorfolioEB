from beanie import Document, Indexed
from pydantic import Field, EmailStr, validator
from uuid import UUID, uuid4
from typing import List, Dict, Optional
from datetime import datetime
from src.models.project_model import Project
from src.models.skill_model import Skill


class Porfolio(Document):
    porfolio_id: UUID = Field(default_factory=uuid4)
    # Login
    username: Indexed(str, unique=True)
    email: Indexed(EmailStr, unique=True)
    password: str

    # Normal Data
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    title: Optional[Dict[str, str]] = None
    phone: Optional[str] = None
    description: Optional[Dict[str, str]] = None
    country: Optional[str] = None
    province: Optional[str] = None

    # Porfolio
    projects: Optional[List[Project]] = None
    skills: Optional[List[Skill]] = None

    # Creation
    date_creation: datetime
    date_modified: datetime

    def __repr__(self) -> str:
        return f"<Porfolio {self.username}>"

    def __str__(self) -> str:
        return self.username

    def __hash__(self) -> int:
        return hash(self.username)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Porfolio):
            return self.username == other.username
        return False

    @property
    def create(self) -> datetime:
        return self.id.generation_time

    @classmethod
    async def by_email(self, email: str) -> "Porfolio":
        return await self.find_one(self.email == email)

    async def by_username(self, username: str) -> "Porfolio":
        return await self.find_one(self.username == username)