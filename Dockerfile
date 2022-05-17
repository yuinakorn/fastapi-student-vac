# linux
#FROM python:3.10.1-slim@sha256:cde92a0c681857e64c2743785c0cd3df02eec53446d7f1535220d42ed9b93c03

# m1
FROM python:3.10.1-slim

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]