from typing import List, Dict
from pydantic import BaseModel, Field, validator
from datetime import datetime
from .validators import validate_date_not_in_future

class Project(BaseModel):
    id: str
    name: Dict[str, str]
    description: Dict[str, str]
    technologies_used: List[str]
    repo_link: str
    date_start: datetime
    date_finish: datetime
    date_created: datetime
    date_modified: datetime
    
    @validator('date_created', 'date_modified')
    def date_not_in_future(cls, v):
        return validate_date_not_in_future(cls, v)