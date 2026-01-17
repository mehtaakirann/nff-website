from sqlalchemy import Column, Integer, String
from database import Base


class FilmSubmission(Base):
    _tablename_ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    director = Column(String, nullable=False)
    age_group = Column(String, nullable=False)
    link = Column(String, nullable=False)


class Registration(Base):
    _tablename_ = "registrations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    role = Column(String, nullable=False)
