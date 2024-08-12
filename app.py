import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from Backend.Connections.VRd_db_loader import DataBase
from Backend.Routes.VRr_api_routers import router


app = FastAPI()
app.mount("/ui", StaticFiles(directory="ui"), name="ui")
templates = Jinja2Templates(directory="ui/screens")

# Include the router
app.include_router(router)


# load the database
db = DataBase()
db.initialize_database()
