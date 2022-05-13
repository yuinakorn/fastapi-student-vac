from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from configure.database import get_db
from models.student_model import StudentDisplayBase
from routes.student import student_controller

router = APIRouter(prefix="/student", tags=["student"])


@router.get("/{cid}", response_model=StudentDisplayBase)
def student_by_id(cid: str, db: Session = Depends(get_db), authorization: str | None = Header(None)):
    return student_controller.read_student_by_cid(db, cid, authorization)
