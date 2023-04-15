from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str