from fastapi import FastAPI
from routes.porfolio import Porfolio
app = FastAPI()
app.include_router(Porfolio)