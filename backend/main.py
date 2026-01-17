from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base, FilmSubmission, Registration
from schemas import FilmCreate, RegisterCreate

app = FastAPI(title="NFF API")

Base.metadata.create_all(bind=engine)


@app.post("/submit-film")
def submit_film(film: FilmCreate):
    db = SessionLocal()
    new_film = FilmSubmission(
        title=film.title,
        director=film.director,
        age_group=film.age_group,
        link=film.link
    )
    db.add(new_film)
    db.commit()
    db.refresh(new_film)
    db.close()
    return {"status": "Film saved successfully"}


@app.post("/register")
def register_user(user: RegisterCreate):
    db = SessionLocal()
    new_user = Registration(
        name=user.name,
        email=user.email,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return {"status": "User registered successfully"}