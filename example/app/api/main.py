from fastapi import FastAPI
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Example FastAPI App"
    debug: bool = False
    version: str = "0.1.0"

    class Config:
        env_file = "../.env"


settings = Settings()
app = FastAPI(title=settings.app_name, version=settings.version, debug=settings.debug)


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Example"}


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "app_name": settings.app_name,
        "version": settings.version,
    }
