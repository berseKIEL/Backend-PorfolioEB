from typing import List, Dict
from pydantic import BaseModel, Field, validator
from datetime import datetime
from enum import Enum


class Skill(BaseModel):
    class ProficiencyEnum(str, Enum):
        beginner = 'Beginner'
        intermediate = 'Intermediate'
        advanced = 'Advanced'

    id: str
    name: str
    proficiency: ProficiencyEnum
    date_created: datetime
    date_modified: datetime


""" 
Format

{
    "name": "Javascript",
    "proficiency": "Intermediate"
},

"""
