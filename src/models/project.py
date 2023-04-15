from typing import List, Dict
from pydantic import BaseModel
from datetime import datetime

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