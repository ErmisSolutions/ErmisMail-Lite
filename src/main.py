from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values
from .email import Emailer

config = dotenv_values()
emailer = Emailer(config["EMAIL_HOST"], config["EMAIL_SMTP_PORT"], config["EMAIL_USERNAME"], config["EMAIL_PASSWORD"])

app = FastAPI()

cors = config["CORS"]

@app.get("/")
async def root():
    return {"message": "Hello World"}