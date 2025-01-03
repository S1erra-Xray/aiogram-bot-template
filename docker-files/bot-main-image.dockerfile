FROM bot-base-image:latest
LABEL authors="S1erra-Xray"

CMD redis-server

ENV proj_name="aiogram_bot_template"

WORKDIR /home/$proj_name/$proj_name

COPY $proj_name/ ./
COPY [ "poetry.lock", "pyproject.toml", ".env", "bot.py", "../" ]

CMD redis-server \
	&& poetry run python /home/$proj_name/bot.py

