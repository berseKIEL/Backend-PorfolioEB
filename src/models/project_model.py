from typing import List, Dict, Optional
from pydantic import Field
from datetime import datetime
from beanie import Document
from uuid import UUID, uuid4


class Project(Document):
    project_id: UUID = Field(default_factory=uuid4)
    name: Dict[str, str]
    description: Dict[str, str]
    technologies_used: List[str]
    repo_link: Optional[str]
    image_link: Optional[List[str]]
    date_start: datetime
    date_finish: Optional[datetime] = None

    date_created: datetime = datetime.now()
    date_modified: datetime = datetime.now()

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
