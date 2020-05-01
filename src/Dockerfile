FROM python
LABEL maintainer="blackd0t@protonmail.com"

WORKDIR /code
COPY . /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
