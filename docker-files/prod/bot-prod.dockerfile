FROM python:3.12.8-alpine3.20
LABEL authors="S1erra-Xray"

RUN apk --update add poetry

ENV directory="aiogram_bot_template"
ENV TYPE="release"
ENV cmd_file="docker-cmd.sh"

WORKDIR /home/bot

COPY poetry.lock poetry.toml pyproject.toml ./
RUN rm /usr/lib/python3.*/EXTERNALLY-MANAGED &>/dev/null; \
    poetry install

COPY $directory ./$directory
COPY bot.py ./
COPY bot_env/bot_prod.env ./bot.env

CMD poetry run python bot.py
