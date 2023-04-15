from typing import List, Dict
from pydantic import BaseModel
from datetime import datetime

class Skill(BaseModel):
    id: str
    name: Dict[str, str]
    proficiency: str
    date_created: datetime
    date_modified: datetime