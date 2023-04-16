from typing import List
from src.models.user_model import User
from src.models.skill_model import Skill
from src.schemas.skill_schema import SkillCreate, SkillUpdate
from uuid import UUID


class SkillService:
    @staticmethod
    async def list_skills(user: User) -> List[Skill]:
        skills = await Skill.find(Skill.owner.id == user.id).to_list()
        return skills

    @staticmethod
    async def create_skill(data: SkillCreate, user: User) -> Skill:
        skill = Skill(**data.dict(), owner=user)
        return await skill.insert()

    @staticmethod
    async def get_skill(skill_id: UUID, user: User) -> Skill:
        skill = await Skill.find_one(Skill.skill_id == skill_id, Skill.owner.id == user.id)
        return skill

    @staticmethod
    async def update_skill(skill_id: UUID, user: User, data: SkillUpdate):
        skill = await SkillService.get_skill(skill_id, user.id)
        await skill.update({"$set": data.dict(exclude_unset=True)})
        await skill.save()
        return skill

    @staticmethod
    async def delete_skill(skill_id: UUID, user: User):
        skill_id_deleted = ''

        skill = await SkillService.get_skill(skill_id, user)
        if skill:
            skill_id_deleted = skill.skill_id
            await skill.delete()

        return {'response': f'{skill_id_deleted} deleted'}
