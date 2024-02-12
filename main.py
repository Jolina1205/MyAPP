from fastapi import FastAPI, Path , Query
from pydantic import BaseModel
from typing import Optional, List
from api import users , courses , section
from DB.DB_setup import engine
from DB.models import user, course, mixins

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Gwen",
        "email": "gwen@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(section.router)

