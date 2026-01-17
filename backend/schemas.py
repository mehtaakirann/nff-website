from pydantic import BaseModel, EmailStr


class FilmSubmission(BaseModel):
    title: str
    director: str
    age_group: str
    link: str


class SponsorInterest(BaseModel):
    name: str
    email: EmailStr
    message: str | None = None


class ContactMessage(BaseModel):
    name: str
    email: EmailStr
    message: str
