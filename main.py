from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from student_database import Base, engine
from student_controller import routers as student_router
from fastapi.staticfiles import StaticFiles

Base.metadata.create_all(bind = engine)
app = FastAPI(title= "Students Result Mangement") 
app.include_router(student_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)