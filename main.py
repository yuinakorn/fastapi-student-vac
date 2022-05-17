from fastapi import FastAPI

from routes.student import student_router
from routes.token import token_router

description = "COVID-19 Immunization Data [RMUTL's Student]"

app = FastAPI(
    title="CMPHO API",
    description=description,
    version="1.0",
)

app.include_router(token_router.router)
app.include_router(student_router.router)


@app.get("/", tags=["/"])
async def welcome():
    return {"message": "Student Vaccine API"}

