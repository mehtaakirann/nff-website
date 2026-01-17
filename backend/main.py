from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import FilmSubmission, SponsorInterest, ContactMessage
from email_service import send_email

app = FastAPI(title="NCFF API")

# CORS (frontend → backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later restrict domain
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"status": "NCFF backend running"}


@app.post("/submit-film")
def submit_film(data: FilmSubmission):
    send_email(
        "New Film Submission",
        f"""
        Title: {data.title}
        Director: {data.director}
        Age Group: {data.age_group}
        Link: {data.link}
        """
    )
    return {"message": "Film submitted successfully"}


@app.post("/sponsor-interest")
def sponsor_interest(data: SponsorInterest):
    send_email(
        "New Sponsor Interest",
        f"""
        Name: {data.name}
        Email: {data.email}
        Message: {data.message}
        """
    )
    return {"message": "Sponsor interest received"}


@app.post("/contact")
def contact(data: ContactMessage):
    send_email(
        "New Contact Message",
        f"""
        Name: {data.name}
        Email: {data.email}
        Message: {data.message}
        """
    )
    return {"message": "Thank you for contacting us"}
