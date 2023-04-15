from fastapi import APIRouter

from models.porfolio import Porfolio
from config.connection import conn
from schemas.porfolio import porfolioEntity

porfolio = APIRouter()

@porfolio.get('/')
async def find_my_porfolio():
    return porfolioEntity(conn.local.porfolio.find())