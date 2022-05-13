import requests
from decouple import config


def get_your_token(password_hash: str, user: str):
    hcode = config('HCODE')
    MOPH_URL_TOKEN = config('MOPH_URL_TOKEN')
    url = f"{MOPH_URL_TOKEN}&user={user}&password_hash={password_hash}&hospital_code={hcode}"

    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    return {"token": response.text}
