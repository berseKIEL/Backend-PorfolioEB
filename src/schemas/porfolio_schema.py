from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict, Optional
from uuid import UUID


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
