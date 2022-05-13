from fastapi import HTTPException
from sqlalchemy.orm import Session  # to get database
from models.student_model import DbStudent
from fastapi.responses import JSONResponse
from decouple import config
import requests
import urllib3

urllib3.disable_warnings()


def read_student_by_cid(db: Session, cid: str, authorization: str):
    result = db.query(DbStudent).filter(DbStudent.cid == cid).first()
    if result is not None:
        result = get_vaccine(cid, authorization)
        return JSONResponse(result)
    else:
        raise HTTPException(status_code=404, detail=f"{cid} not found in database.")


def get_vaccine(cid: str, authorization: str):
    MOPH_URL_TARGET = config('MOPH_URL_TARGET')
    hcode = config('HCODE')
    url = f"{MOPH_URL_TARGET}?cid={cid}&hospital_code={hcode}"

    payload = {}
    headers = {
        'Authorization': authorization
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    return response.json()
