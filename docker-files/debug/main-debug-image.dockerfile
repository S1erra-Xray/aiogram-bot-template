FROM base-debug-image:latest
LABEL authors="S1erra-Xray"

ARG directory="aiogram_bot_template"

WORKDIR /home/$directory/$directory

COPY $directory/ ./ \
	 bot.py ../

COPY bot_env/bot_debug.env ../bot.env

RUN redis-server &
CMD poetry run python /home/$directory/bot.py

