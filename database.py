# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy

DATABASE_URL = "sqlite:///./test.db"  # change this to your actual database URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = sqlalchemy.ext.declarative.declarative_base()
