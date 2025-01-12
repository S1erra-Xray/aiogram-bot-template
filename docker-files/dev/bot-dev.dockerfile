FROM python:3.12.8-alpine3.20

ENV TYPE="debug"

RUN apk --update add poetry
WORKDIR /home/bot

COPY poetry.lock poetry.toml pyproject.toml ./
RUN rm /usr/lib/python3.*/EXTERNALLY-MANAGED &>/dev/null; \
    poetry install

CMD poetry run python bot.py
