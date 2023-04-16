from pydantic import BaseModel, EmailStr
from typing import Dict, List
from uuid import UUID
from src.schemas.project_schema import ProjectOut
from src.schemas.skill_schema import SkillOut
from src.schemas.user_schema import UserSchemaOut

class PorfolioSchemaOut(BaseModel):
    # User Data
    user: UserSchemaOut
    # CVData
    skills: List[SkillOut]
    projects: List[ProjectOut]