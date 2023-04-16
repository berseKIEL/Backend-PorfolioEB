from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from uuid import UUID
from datetime import datetime


class DescriptionProject:
    en: str = Field(..., title="Description EN", min_length=2, max_length=50)
    es: str = Field(..., title="Descripción ES", min_length=2, max_length=50)


class ProjectCreate(BaseModel):
    name: str = Field(..., title="Name", min_length=2, max_length=50)
    description: Dict[DescriptionProject] = Field(..., title="Description")
    technologies_used: List[str]
    repo_link: str
    image_link: List[str]
    date_start: datetime
    date_finish: Optional[datetime] = None


class ProjectUpdate(BaseModel):
    name: Optional[str] = Field(..., title="Name", min_length=2, max_length=50)
    description: Optional[Dict[DescriptionProject]] = Field(..., title="Description")
    technologies_used: Optional[List[str]]
    repo_link: Optional[str] = Field(..., title="Repository Link", min_length=2, max_length=120)
    image_link: Optional[List[str]]
    date_start: Optional[datetime]
    date_finish: Optional[datetime]

class ProjectOut(BaseModel):
    project_id: UUID
    name: Dict[str, str]
    description: Dict[str, str]
    technologies_used: List[str]
    repo_link: Optional[str]
    image_link: Optional[List[str]]
    date_start: datetime
    date_finish: Optional[datetime] = None

    created_at: datetime
    updated_at: datetime
