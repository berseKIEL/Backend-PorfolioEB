from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime
from src.models.skill_model import ProficiencyEnum


class SkillCreate(BaseModel):
    name: str = Field(..., title="Name", min_length=2, max_length=50)
    profiency: ProficiencyEnum = Field(..., title="Proficiency")


class SkillUpdate(BaseModel):
    name: Optional[str] = Field(..., title="Name", min_length=2, max_length=50)
    profiency: Optional[ProficiencyEnum] = Field(..., title="Proficiency")


class SkillOut(BaseModel):
    name: str
    profiency: str
