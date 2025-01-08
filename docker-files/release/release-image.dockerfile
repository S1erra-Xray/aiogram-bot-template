FROM postgres:17.2-alpine3.21
LABEL authors="S1erra-Xray"

RUN apk --update add redis python3 poetry

ENV directory="aiogram_bot_template"

WORKDIR /home/bot

ADD poetry.lock ./
ADD	pyproject.toml ./
ADD	poetry.toml ./

RUN rm /usr/lib/python3.*/EXTERNALLY-MANAGED
RUN poetry install
RUN redis-server &

ADD $directory ./$directory
ADD bot.py ./
ADD bot_env/bot_release.env ./bot.env

CMD poetry run python /home/bot/bot.py