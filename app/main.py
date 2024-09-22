from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .db.session import init_db
from .api.auth import auth_router
from .api.v1 import api_router
from .routes.v1 import web_router

init_db()

app = FastAPI()

# templates = Jinja2Templates(directory="app/templates")

# Servir les fichiers statiques
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configurer les routes
app.include_router(auth_router)
app.include_router(api_router)
app.include_router(web_router)
