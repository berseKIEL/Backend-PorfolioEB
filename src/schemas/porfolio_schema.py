from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict, Optional
from uuid import UUID
from src.models.project_model import Project
from src.models.skill_model import Skill


class UserPorfolioSchemaIn(BaseModel):
    # Login Data
    email: EmailStr = Field(..., description="Email")
    username: str = Field(..., min_length=5,
                          max_length=50, description="Username")
    password: str = Field(..., min_length=5, max_length=25,
                          description="Password")


class UserPorfolioSchemaOut(BaseModel):
    porfolio_id: UUID
    email: str
    username: str


class PorfolioSchema(BaseModel):
    # Login
    username: str
    email: str

    # Normal Data
    first_name: str = None
    last_name: str = None
    title: Dict[str, str] = None
    phone: str = None
    description: Dict[str, str] = None
    country: str = None
    province: str = None

    # Porfolio
    projects: List[Project] = None
    skills: List[Skill] = None


class PorfolioNormalData(BaseModel):
    first_name: str
    last_name: str
    title: Dict[str, str]
    phone: str
    description: Dict[str, str]
    country: str
    province: str
