from sqlalchemy import Column, Integer, String
from database import Base

class FilmSubmission(Base):
    _tablename_ = "submissions"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    age_group = Column(String)
    link = Column(String)