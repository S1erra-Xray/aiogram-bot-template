FROM base-debug-image:latest
LABEL authors="S1erra-Xray"

ENV directory="aiogram_bot_template"

WORKDIR /home/bot

ADD $directory ./$directory
ADD	bot.py ./
ADD bot_env/bot_debug.env ./bot.env

#CMD sleep 10000
