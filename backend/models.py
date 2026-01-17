from sqlalchemy import Column, Integer, String
from database import Base


class FilmSubmission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    director = Column(String)
    age_group = Column(String)
    link = Column(String)


class Registration(Base):
    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)