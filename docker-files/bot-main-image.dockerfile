FROM bot-base-image:latest
LABEL authors="S1erra-Xray"

ENV directory="aiogram_bot_template"

WORKDIR /home/$directory/$directory

COPY $directory/ ./
COPY [ "poetry.lock", "pyproject.toml", "bot.env", "bot.py", "../" ]

RUN redis-server &
CMD poetry run python /home/$directory/bot.py

