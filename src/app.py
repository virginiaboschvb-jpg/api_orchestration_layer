from fastapi import FastAPI
from src.config.router import router
from src.config.settings import Settings

app = FastAPI(title="API Orchestration Layer")

# Load settings
settings = Settings()

# Register routes
app.include_router(router)
