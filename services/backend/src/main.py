from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.db import engine, database, metadata
from src.routes import users, sportactivities


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(sportactivities.router)

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()



@app.get("/")
async def home():
    return "Hello, World from FastAPI backend!"