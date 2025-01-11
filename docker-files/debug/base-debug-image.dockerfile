FROM postgres:17.2-alpine3.21
LABEL authors="S1erra-Xray"

RUN apk --update add redis python3 poetry
WORKDIR /home/bot

ADD poetry.lock ./
ADD	pyproject.toml ./
ADD	poetry.toml ./

RUN rm /usr/lib/python3.*/EXTERNALLY-MANAGED \
	&& poetry install

#CMD sleep 1000000