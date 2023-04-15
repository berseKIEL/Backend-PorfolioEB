from pydantic import BaseModel

class Porfolio(BaseModel):
    description: str
    title: str
    email: str
    phone: str
    location: str