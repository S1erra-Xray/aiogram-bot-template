FROM base-debug-image:latest
LABEL authors="S1erra-Xray"

ENV directory="aiogram_bot_template"
ENV cmd_file="docker-cmd.sh"
ENV TYPE="debug"

WORKDIR /home/bot

ADD $directory ./$directory
ADD bot.py docker-files/$cmd_file ./
ADD bot_env/bot_debug.env ./bot.env

CMD ./$cmd_file

#CMD sleep 10000