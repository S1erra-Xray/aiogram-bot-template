FROM postgres:17.2-alpine3.21
LABEL authors="S1erra-Xray"

RUN apk --update add redis python3 poetry

ENV cmd_file="docker-cmd.sh"
ENV WORKDIR="/home/bot"
ENV TYPE=""