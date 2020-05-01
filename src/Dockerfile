FROM python:3.7-slim

LABEL maintainer="blackd0t@protonmail.com"

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "bot.py"]
