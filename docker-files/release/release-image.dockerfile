FROM postgres:17.2-alpine3.21
LABEL authors="S1erra-Xray"

ADD poetry.lock ./ \
	pyproject.toml ./ \
	poetry.toml ./

RUN apk --update add redis python3 poetry \
    && rm /usr/lib/python3.*/EXTERNALLY-MANAGED \
    && poetry install \
    && redis-server &

ARG directory="aiogram_bot_template"
WORKDIR /home/$directory/$directory

COPY $directory/ ./ \
	 bot.py ../

COPY bot_env/bot_release.env ../bot.env

CMD poetry run python /home/$directory/bot.py