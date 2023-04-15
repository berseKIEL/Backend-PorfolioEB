from typing import List, Dict
from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class Skill(BaseModel):
    class ProficiencyEnum(str, Enum):
        beginner = 'Beginner'
        intermediate = 'Intermediate'
        advanced = 'Advanced'

    name: str
    proficiency: ProficiencyEnum

    date_created: datetime = datetime.now()
    date_modified: datetime = datetime.now()


""" 
Format

{
    "name": "Javascript",
    "proficiency": "Intermediate"
},

"""
