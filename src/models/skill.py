from typing import List, Dict
from pydantic import BaseModel, Field, validator
from datetime import datetime
from enum import Enum
from .validators import validate_date_not_in_future

class Skill(BaseModel):
    class ProficiencyEnum(str, Enum):
        beginner = 'beginner'
        intermediate = 'intermediate'
        advanced = 'advanced'
        
    id: str
    name: Dict[str, str]
    proficiency: ProficiencyEnum
    date_created: datetime
    date_modified: datetime
    
    @validator('date_created', 'date_modified')
    def date_not_in_future(cls, v):
        return validate_date_not_in_future(cls, v)