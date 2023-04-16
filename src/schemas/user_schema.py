from pydantic import BaseModel, Field, EmailStr
from typing import Dict
from uuid import UUID
from datetime import datetime


class UserSchemaIn(BaseModel):
    # Login Data
    email: EmailStr = Field(..., description="Email")
    username: str = Field(..., min_length=5,
                          max_length=50, description="Username")
    password: str = Field(..., min_length=5, max_length=25,
                          description="Password")


class UpdateUser(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    title: Dict[str, str]
    phone: str
    description: str
    country: str
    province: str


class UserSchemaOut(BaseModel):
    user_id: UUID
    email: str
    username: str
    first_name: str = None
    last_name: str = None
    title: Dict[str, str] = None
    phone: str = None
    description: Dict[str, str] = None
    country: str = None
    province: str = None
