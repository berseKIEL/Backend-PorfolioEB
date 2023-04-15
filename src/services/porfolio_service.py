from src.models.porfolio_model import Porfolio
from typing import List


class PorfolioService():
    @staticmethod
    async def get_all_porfolio() -> List[Porfolio]:
        portfolio = await Porfolio.all().to_list()
        print(portfolio)
        return portfolio
    
    @staticmethod
    async def get_porfolio(email: str) -> Porfolio:
        porfolio = await Porfolio.find()
        return porfolio