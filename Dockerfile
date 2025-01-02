FROM python:3.10-alpine3.21
LABEL authors="S1erra-Xray"

ENV proj_name="aiogram_bot_template"

WORKDIR /home/$proj_name/$proj_name

COPY $proj_name/ ./
COPY [ "poetry.lock", "pyproject.toml", "env", "bot.py", "../" ]

RUN pip install poetry \
	&& poetry config virtualenvs.create false \
	&& poetry install

CMD ["sleep", "10000"]
CMD ["sh", "-c", "poetry run python /home/$proj_name/bot.py"]


