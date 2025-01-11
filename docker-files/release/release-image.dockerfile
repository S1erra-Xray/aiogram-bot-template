FROM postgres:17.2-alpine3.21
LABEL authors="S1erra-Xray"

RUN apk --update add redis python3 poetry

ENV directory="aiogram_bot_template"
ENV cmd_file="docker-cmd.sh"
ENV TYPE="release"

WORKDIR /home/bot

ADD poetry.lock poetry.toml pyproject.toml ./
RUN rm /usr/lib/python3.*/EXTERNALLY-MANAGED \
    && poetry install

ADD $directory ./$directory
ADD	bot.py docker-files/$cmd_file ./
ADD bot_env/bot_release.env ./bot.env

CMD ./$cmd_file
