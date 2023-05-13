from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM



# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")

"""
import 'from src.routes import users, sportactivities' must be after 'Tortoise.init_models'
why?
https://stackoverflow.com/questions/65531387/tortoise-orm-for-python-no-returns-relations-of-entities-pyndantic-fastapi
"""
from src.routes import users, sportactivities


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(sportactivities.router)


# Call the function for registering and configuring Tortoise with the essential parameters
register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)


@app.get("/")
async def home():
    return "Hello, World from FastAPI backend!"