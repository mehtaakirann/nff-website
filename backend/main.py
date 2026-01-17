from fastapi import FastAPI
from database import SessionLocal, engine
from models import Base, FilmSubmission, Registration
from schemas import FilmCreate, RegisterCreate

app = FastAPI(title="NFF API")
Base.metadata.create_all(bind=engine)

@app.post("/submit-film")
def submit_film(film: FilmCreate):
    db = SessionLocal()
    new_film = FilmSubmission(**film.dict())
    db.add(new_film)
    db.commit()
    return {"status": "Film saved"}

@app.post("/register")
def register_user(user: RegisterCreate):
    db = SessionLocal()
    new_user = Registration(**user.dict())
    db.add(new_user)
    db.commit()
    return {"status": "User registered"}
