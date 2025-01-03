FROM postgres:17.2-alpine3.21
LABEL authors="S1erra-Xray"

RUN apk --update add redis python3 py3-pip poetry
WORKDIR /tmp
ADD poetry.lock .
ADD pyproject.toml .
RUN rm /usr/lib/python3.*/EXTERNALLY-MANAGED \
    && poetry export --without-hashes --format=requirements.txt > requirements.txt \
	&& pip install -r requirements.txt
