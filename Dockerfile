FROM python:3.11-alpine
LABEL authors="onelots"


ENV LANG fr_FR.UTF-8
WORKDIR /app
COPY . /app
LABEL authors="onelots"

RUN pip install -r requirements.txt


CMD [ "python", "main.py" ]