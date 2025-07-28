from fastapi import FastAPI
from src import filter_router
from src.core import database_conn
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

@app.on_event("startup")
async def startup():
    await database_conn.connect()

@app.on_event("shutdown")
async def shutdown():
    await database_conn.disconnect()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(filter_router, prefix="/filters") 
