FROM bot-base-image:latest
LABEL authors="S1erra-Xray"

CMD redis-server

ENV directory="TGBot"

WORKDIR /home/$directory/$directory

COPY $directory/ ./
COPY [ "poetry.lock", "pyproject.toml", ".env", "bot.py", "../" ]

CMD redis-server \
	&& poetry run python /home/$directory/bot.py

