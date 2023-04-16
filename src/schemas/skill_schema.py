from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class SkillCreate(BaseModel):
    name: str = Field(..., title="Name", min_length=2, max_length=50)
    level: int = Field(..., title="Level")


class SkillUpdate(BaseModel):
    name: Optional[str] = Field(..., title="Name", min_length=2, max_length=50)
    level: Optional[int] = Field(..., title="Level")
    
class SkillOut(BaseModel):
    skill_id: UUID
    name: str
    level: str
    created_at: datetime
    updated_at: datetime