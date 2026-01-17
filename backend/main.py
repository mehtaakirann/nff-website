from fastapi import FastAPI
from models import Base
from database import engine

app = FastAPI(title="NFF API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "NFF Backend Running"}
