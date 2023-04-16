from fastapi import APIRouter, Depends
from typing import List
from src.routes.deps.user_deps import get_current_user
from src.schemas.project_schema import ProjectOut, ProjectCreate, ProjectUpdate
from src.models.user_model import User
from src.models.project_model import Project
from src.services.project_service import ProjectService
from uuid import UUID


project_handler = APIRouter()


@project_handler.get('/', summary="Obtiene las habilidades de un usuario", response_model=List[ProjectOut])
async def list_projects(current_user: User = Depends(get_current_user)):
    return await ProjectService.list_projects(current_user)


@project_handler.post('/create', summary="Crea habilidades para un usuario", response_model=Project)
async def create_project(data: ProjectCreate, current_user: User = Depends(get_current_user)):
    return await ProjectService.create_project(data, current_user)


@project_handler.get('/{project_id}', summary="Obtiene una habilidad por su id", response_model=ProjectOut)
async def get_project(project_id: UUID, current_user: User = Depends(get_current_user)):
    return await ProjectService.get_project(project_id, current_user)


@project_handler.put('/{project_id}', summary="Edita la habilidad de un usuario según su ID", response_model=ProjectOut)
async def update_project(project_id: UUID, data: ProjectUpdate, current_user: User = Depends(get_current_user)):
    return await ProjectService.update_project(project_id, current_user, data)


@project_handler.delete('/{project_id}', summary="Borra una habilidad de un usuario según su ID")
async def delete_project(project_id: UUID, current_user: User = Depends(get_current_user)):
    return await ProjectService.delete_project(project_id, current_user)
