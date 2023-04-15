from typing import List, Dict, Optional
from pydantic import BaseModel
from datetime import datetime


class Project(BaseModel):
    name: Dict[str, str]
    description: Dict[str, str]
    technologies_used: List[str]
    repo_link: Optional[str]
    date_start: datetime
    date_finish: Optional[datetime] = None

    date_created: datetime = datetime.now()
    date_modified: datetime = datetime.now()


""" 
Format

{
    "name": {
        "en": "",
        "es": ""
    },
    "description": {
        "en": "",
        "es": ""
    },
    "technologies_used": [
        ""
    ],
    "date_start": "",
    "date_finish": "",
}
"""
