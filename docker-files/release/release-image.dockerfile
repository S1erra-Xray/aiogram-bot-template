FROM base-image:latest
LABEL authors="S1erra-Xray"

RUN apk --update add redis python3 poetry

ENV directory="aiogram_bot_template"
ENV TYPE="release"

WORKDIR $WORKDIR

ADD poetry.lock poetry.toml pyproject.toml ./
RUN rm /usr/lib/python3.*/EXTERNALLY-MANAGED &>/dev/null; \
    poetry install

ADD $directory ./$directory
ADD	bot.py docker-files/$cmd_file ./
ADD bot_env/bot_release.env ./bot.env

CMD ./$cmd_file
