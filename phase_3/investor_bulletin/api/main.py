from uvicorn import run
from fastapi import FastAPI

from dotenv import load_dotenv

from api.routes import init_routes

app = init_routes(FastAPI())
load_dotenv()

if __name__ == "__main__":
    run("api.main:app")
