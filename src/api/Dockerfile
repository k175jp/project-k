FROM python:3.11-bullseye

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app/ /app/src

WORKDIR /app/src

CMD uvicorn app:app --host "0.0.0.0" --port 30800 --reload