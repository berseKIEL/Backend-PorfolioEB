from pydantic import BaseModel, Field, validator
from uuid import UUID
from typing import List, Dict
from datetime import datetime
from project import Project
from skill import Skill
from .validators import validate_date_not_in_future

class Porfolio(BaseModel):
    id: UUID
    # Login
    username: str = Field(..., min_length=6, max_length=32)
    email: str = Field(..., regex=r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    password: str
    
    # Normal Data
    first_name: str
    last_name: str
    title: Dict[str, str]
    phone: str
    description: str
    country: str
    province: str
        
    # Porfolio
    projects: List[Project]
    skills: List[Skill]
    
    # Creation
    date_creation: datetime
    date_modified: datetime
    
    @validator('date_created', 'date_modified')
    def date_not_in_future(cls, v):
        return validate_date_not_in_future(cls, v)
    
PorfolioSchema = Porfolio.schema()