from beanie import Document
from pydantic import Field
from uuid import UUID, uuid4

class Skill(Document):
    skill_id: UUID = Field(default_factory=uuid4)
    user_id: UUID
    name: str
    level: int

    def __repr__(self) -> str:
        return f"<Skill {self.name}>"

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Skill):
            return self.name == other.name
        return False