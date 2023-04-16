from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from uuid import UUID
from datetime import datetime
from src.models.general_model import Translation

class ProjectCreate(BaseModel):
    name: Optional[Translation] = Field(..., title="Name")
    description: Optional[Translation] = Field(..., title="Description")
    technologies_used: List[str]
    repo_link: str
    image_link: List[str]
    date_start: datetime
    date_finish: Optional[datetime]


class ProjectUpdate(BaseModel):
    name: Optional[Translation] = Field(..., title="Name")
    description: Optional[Translation] = Field(..., title="Description")
    technologies_used: Optional[List[str]]
    repo_link: Optional[str] = Field(..., title="Repository Link",
                                     min_length=2, max_length=120)
    image_link: Optional[List[str]]
    date_start: Optional[datetime]
    date_finish: Optional[datetime]


class ProjectOut(BaseModel):
    name: Optional[Translation]
    description: Optional[Translation]
    technologies_used: List[str]
    repo_link: Optional[str]
    image_link: Optional[List[str]]
    date_start: datetime
    date_finish: Optional[datetime] = None

    created_at: datetime
    updated_at: datetime
