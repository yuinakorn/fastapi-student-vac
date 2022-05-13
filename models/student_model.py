from pydantic import BaseModel
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from decouple import config

from configure.database import Base


class DbStudent(Base):
    __tablename__ = config('SECRET_TBL')
    # id = Column(Integer, primary_key=True, index=True)
    cid = Column(String, unique=True, primary_key=True, index=True)


class StudentBase(BaseModel):
    cid: str


class StudentDisplayBase(BaseModel):
    result: str

    class Config:
        orm_mode = True
