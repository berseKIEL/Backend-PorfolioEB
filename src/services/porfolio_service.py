from fastapi import HTTPException, status
from src.services.user_service import UserService
from src.services.skill_service import SkillService
from src.services.project_service import ProjectService


class PorfolioService():
    @staticmethod
    async def get_porfolio(username: str):
        porfolio = {}
        
        userData = await UserService.get_user(username)

        if userData:
            porfolio['user'] = userData
            skills = await SkillService.list_skills(userData)
            projects = await ProjectService.list_projects(userData)
            porfolio['skills'] = skills
            porfolio['projects'] = projects

        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No existe un porfolio valido de ese usuario"
            )
        return porfolio
