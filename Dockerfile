FROM python:3.10-slim-buster

COPY .env ./env.list

RUN apt-get upgrade
RUN python -m pip install --upgrade pip

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app
WORKDIR /app

ENTRYPOINT "python" "main.py"
#CMD ["uvicorn", "main:app"]
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]