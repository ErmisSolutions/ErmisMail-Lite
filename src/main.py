import os
from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from dotenv import find_dotenv, load_dotenv
from src.apiemail import Emailer
from src.apiconfig import APIConfig
from typing_extensions import Annotated

load_dotenv(find_dotenv())

apiSettings = APIConfig()
env = os.environ
emailer = Emailer(env["EMAIL_HOST"], env["EMAIL_SMTP_PORT"], env["EMAIL_USERNAME"], env["EMAIL_PASSWORD"])

app = FastAPI()

cors = env["CORS"]

@app.get("/")
async def root(request: Request):
    print(request.client.host)
    return {"message": f'{request.headers["host"]}'}

@app.post("/email/{key}")
async def email(key, fromEmail: Annotated[str, Form()], messageBody: Annotated[str, Form()]):
    try:
        toEmail = apiSettings.getEmail(key)
        emailer.sendMail(toEmail, fromEmail, messageBody)
    except Exception as ex:
        return {"message: " f'{ex.message}'}