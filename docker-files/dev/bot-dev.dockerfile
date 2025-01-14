FROM python:3.12.8-alpine3.20

RUN apk --update add poetry
WORKDIR /home/bot

COPY poetry.lock poetry.toml pyproject.toml ./

RUN rm /usr/lib/python3.*/EXTERNALLY-MANAGED &>/dev/null; \
    poetry install

COPY bot_env/bot_dev.env ./bot.env

CMD ln -s bot_env/bot_dev.env bot.env; poetry run python bot.py