import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import find_dotenv, load_dotenv
from src.apiemail import Emailer
from src.apiconfig import APIConfig
from typing_extensions import Annotated

load_dotenv(find_dotenv())

apiSettings = APIConfig()
env = os.environ
emailer = Emailer(env["EMAIL_HOST"], env["EMAIL_SMTP_PORT"], env["EMAIL_USERNAME"], env["EMAIL_PASSWORD"])

app = FastAPI(root_path=env["BASE_PATH"])

cors = env["CORS"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"]
)

@app.get("/")
async def root(request: Request):
    print(request.client.host)
    return {"message": f'{request.headers["host"]}', "root_path": request.scope.get("root_path")}

@app.post("/{key}")
async def email(key, name: Annotated[str, Form()], fromEmail: Annotated[str, Form()], subject: Annotated[str, Form()], messageBody: Annotated[str, Form()], request: Request):
    try:
        toEmail, redirectUrl = apiSettings.getSettings(key)
        if toEmail is None:
            raise Exception(f'Invalid Key [{key}]')
        if emailer.sendMail(toEmail, name, fromEmail, subject, messageBody):
            if redirectUrl is not None:
                redirectUrl = redirectUrl.replace("?", "?message=EmailSent&success=True")
                return RedirectResponse(redirectUrl)
            else:
                return { "message": f"Email sent", "success": True }
        else:
            return { "message": f"Unknown Error!", "success": False }
    except Exception as ex:
        return { "message": f'{ex.args[0]}', "success": False }