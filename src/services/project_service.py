from typing import List
from src.models.user_model import User
from src.models.project_model import Project
from src.schemas.project_schema import ProjectCreate, ProjectUpdate
from uuid import UUID


class ProjectService:
    @staticmethod
    async def list_projects(user: User) -> List[Project]:
        projects = await Project.find(Project.owner.id == user.id).to_list()
        return projects

    @staticmethod
    async def create_project(data: ProjectCreate, user: User) -> Project:
        project = Project(**data.dict(), owner=user)
        return await project.insert()

    @staticmethod
    async def get_project(project_id: UUID, user: User) -> Project:
        project = await Project.find_one(Project.project_id == project_id, Project.owner.id == user.id)
        return project

    @staticmethod
    async def update_project(project_id: UUID, user: User, data: ProjectUpdate):
        project = await ProjectService.get_project(project_id, user.id)
        await project.update({"$set": data.dict(exclude_unset=True)})
        await project.save()
        return project

    @staticmethod
    async def delete_project(project_id: UUID, user: User):
        project_id_deleted = ''

        project = await ProjectService.get_project(project_id, user)
        if project:
            project_id_deleted = project.project_id
            await project.delete()

        return {'response': f'{project_id_deleted} deleted'}
