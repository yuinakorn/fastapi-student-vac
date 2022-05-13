from fastapi import FastAPI

from routes.student import student_router
from routes.token import token_router

app = FastAPI()

app.include_router(student_router.router)
app.include_router(token_router.router)


@app.get("/", tags=["/"])
async def api():
    return {"message": "Student Vaccine API"}

