from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime
from project import Project
from skill import Skill

class Porfolio(BaseModel):
    id: str
    # Login
    username: str
    email: str
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