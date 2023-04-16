from uuid import UUID, uuid4
from beanie import Document, Link, before_event, Replace, Insert
from typing import List, Dict, Optional
from pydantic import Field
from datetime import datetime
from src.models.user_model import User
from src.models.general_model import Translation

class Project(Document):
    project_id: UUID = Field(default_factory=uuid4, unique=True)
    owner: Link[User]
    name: Optional[Translation]
    description: Optional[Translation]
    technologies_used: List[str]
    repo_link: Optional[str]
    image_link: Optional[List[str]]
    date_start: datetime
    date_finish: Optional[datetime] = None

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Project {self.name}>"

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Project):
            return self.name == other.name
        return False

    @before_event([Replace, Insert])
    def update_updated_at(self):
        self.updated_at = datetime.utcnow()

    class Settings:
        name = 'projects'