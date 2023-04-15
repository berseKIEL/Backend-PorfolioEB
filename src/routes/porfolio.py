from fastapi import APIRouter

from models.porfolio import Porfolio, PorfolioSchema
from config.connection import conn

porfolio = APIRouter()

@porfolio.get('/')
async def find_my_porfolio():
    return PorfolioSchema