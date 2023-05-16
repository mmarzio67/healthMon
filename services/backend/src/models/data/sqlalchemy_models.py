from sqlalchemy import Time, Boolean, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from db_config.sqlalchemy_connect import Base

class Users(Base): 
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, )
    username = Column(String, unique=False, index=False)
    full_name = Column(String, unique=False, index=False)
    password = Column(String, unique=False, index=False)
    created_at = Column(Date, unique=False, index=False)
    modified_at = Column(Date, unique=False, index=False)


class SportActivities(Base):
    __tablename__ = "sportactivities"
    id = Column(Integer, primary_key=True, index=True, )
    title = Column(String, unique=False, index=False)
    content = Column(String, unique=False, index=False) 
    athlete = Column(Integer, ForeignKey('users.id'), unique=False, index=False)
    created_at = Column(Date, unique=False, index=False)
    modified_at = Column(Date, unique=False, index=False)

    athletes = relationship('Users', 
             back_populates="sportactivities")

    def __str__(self):
        return f"{self.title}, {self.athlete_id} on {self.created_at}"
