FROM python:3.9-slim-buster
LABEL authors="mr_akkerman"

WORKDIR /app
COPY . /app

RUN apt-get update

RUN pip install -r requirements.txt
RUN rm -rf /var/lib/apt/lists/*

CMD ["python", "main.py"]
