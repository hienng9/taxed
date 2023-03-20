FROM python:3

ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /usr/src/code

COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt

COPY . .