from fastapi import APIRouter, Depends
from typing import List
from src.routes.deps.user_deps import get_current_user
from src.schemas.skill_schema import SkillOut, SkillCreate, SkillUpdate
from src.models.user_model import User
from src.models.skill_model import Skill
from src.services.skill_service import SkillService
from uuid import UUID


skill_router = APIRouter()


@skill_router.get('/', summary="Obtiene las habilidades de un usuario", response_model=List[SkillOut])
async def list_skills(current_user: User = Depends(get_current_user)):
    return await SkillService.list_skills(current_user)


@skill_router.post('/create', summary="Crea habilidades para un usuario", response_model=Skill)
async def create_skill(data: SkillCreate, current_user: User = Depends(get_current_user)):
    return await SkillService.create_skill(data, current_user)


@skill_router.get('/{skill_id}', summary="Obtiene una habilidad por su id", response_model=SkillOut)
async def get_skill(skill_id: UUID, current_user: User = Depends(get_current_user)):
    return await SkillService.get_skill(skill_id, current_user)


@skill_router.put('/{skill_id}', summary="Edita la habilidad de un usuario según su ID", response_model=SkillOut)
async def update_skill(skill_id: UUID, data: SkillUpdate, current_user: User = Depends(get_current_user)):
    return await SkillService.update_skill(skill_id, current_user, data)


@skill_router.delete('/{skill_id}', summary="Borra una habilidad de un usuario según su ID")
async def delete_skill(skill_id: UUID, current_user: User = Depends(get_current_user)):
    return await SkillService.delete_skill(skill_id, current_user)
