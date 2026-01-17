from sqlalchemy import Column, Integer, String
from database import Base

class FilmSubmission(Base):
    _tablename_ = "submissions"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    age_group = Column(String)
    link = Column(String)

from sqlalchemy import Column, Integer, String
from database import Base

class Registration(Base):
    _tablename_ = "registrations"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)

