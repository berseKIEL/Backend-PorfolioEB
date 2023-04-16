from pydantic import BaseModel, Field, EmailStr
from uuid import UUID


class UserSchemaIn(BaseModel):
    # Login Data
    email: EmailStr = Field(..., description="Email")
    username: str = Field(..., min_length=5,
                          max_length=50, description="Username")
    password: str = Field(..., min_length=5, max_length=25,
                          description="Password")


class UserSchemaOut(BaseModel):
    user_id: UUID
    email: str
    username: str