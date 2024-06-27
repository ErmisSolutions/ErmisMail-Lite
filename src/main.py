from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import Config

app = FastAPI()
config = Config()

cors = config.Cors()

@app.get("/")
async def root():
    return {"message": "Hello World"}