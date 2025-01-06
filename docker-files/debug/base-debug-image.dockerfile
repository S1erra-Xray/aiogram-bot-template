FROM postgres:17.2-alpine3.21
LABEL authors="S1erra-Xray"

RUN apk --update add redis python3 poetry

WORKDIR /home/aiogram_bot_template

ADD poetry.lock ./ \
	pyproject.toml ./ \
	poetry.toml ./

RUN rm /usr/lib/python3.*/EXTERNALLY-MANAGED \
    && poetry install
