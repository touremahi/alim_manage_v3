from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
from .db.session import init_db
from .api.v1 import api_router

init_db()

app = FastAPI()

# Servir les fichiers statiques
# app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api_router)

# Configurer les routes
@app.get("/")
async def root():
    return {"message": "Hello World"}