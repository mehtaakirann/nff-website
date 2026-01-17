from pydantic import BaseModel


class FilmCreate(BaseModel):
    title: str
    director: str
    age_group: str
    link: str


class RegisterCreate(BaseModel):
    name: str
    email: str
    role: str
