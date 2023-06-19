# crud.py
from sqlalchemy.orm import Session
import models, schemas

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, hashed_password=user.password, balance=1000) # here we are assigning 1000 coins to each new user
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# crud.py

def get_game(db: Session, id: int):
    return db.query(models.Game).filter(models.Game.id == id).first()
