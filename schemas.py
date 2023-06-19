# schemas.py
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    balance: int  # this line is new, it will allow you to return the balance to the user
    class Config:
        orm_mode = True
class GameBase(BaseModel):
    name: str
    odds: int

class GameCreate(GameBase):
    pass

class Game(GameBase):
    id: int
    class Config:
        orm_mode = True
