from pydantic import BaseModel, Field, EmailStr
from typing import Dict, Optional
from uuid import UUID
from datetime import datetime


class UserSchemaIn(BaseModel):
    # Login Data
    email: EmailStr = Field(..., description="Email")
    username: str = Field(..., min_length=5,
                          max_length=50, description="Username")
    password: str = Field(..., min_length=5, max_length=25,
                          description="Password")


class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    title: Dict[str, str]
    phone: Optional[str]
    description: Optional[str]
    country: Optional[str]
    province: Optional[str]


class UserSchemaOut(BaseModel):
    email: EmailStr
    username: str
    first_name: str = None
    last_name: str = None
    title: Dict[str, str] = None
    phone: str = None
    description: Dict[str, str] = None
    country: str = None
    province: str = None
