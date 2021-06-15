FROM python:3.9-alpine

RUN apk update && apk add fortune
RUN pip3 install tweepy

COPY fortunebot.py /fortunebot.py

ENTRYPOINT [ "python3", "fortunebot.py" ]