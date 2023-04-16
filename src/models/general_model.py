from pydantic import BaseModel

class Translation(BaseModel):
    en: str
    es: str