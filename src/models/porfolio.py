from pydantic import BaseModel

class Porfolio(BaseModel):
    name: str
    description: str
    title: str
    email: str
    phone: str
    location: str