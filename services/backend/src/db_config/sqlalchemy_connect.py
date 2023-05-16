import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = os.getenv("DATABASE_URL")

engine = create_engine(DB_URL)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()