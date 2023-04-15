from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime

class Porfolio(BaseModel):
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
    county: str
    province: str
        
    # Porfolio
    projects: List[Dict[str, str]]
    skills: List[Dict[str, str]]
    
    # Creation
    date_creation: datetime
    date_modified: datetime
    
    class Config:
        json_encoders = {
            ObjectId: str
        }