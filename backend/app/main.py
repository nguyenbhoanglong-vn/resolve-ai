from fastapi import FastAPI

from .database import Base, engine
from .routers import tickets

from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
     title = "ResolveAI API",
     version = "1.0.0"
)

app.include_router(tickets.router)

@app.get("/")
def root():
     return {
          "message": "ResolveAI API is running"
     }

app.add_middleware(
     CORSMiddleware,
     allow_origins=[
          "http://localhost:5173"
     ],
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)