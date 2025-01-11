FROM base-image:latest

ENV TYPE="debug"

WORKDIR $WORKDIR

ADD poetry.lock poetry.toml pyproject.toml ./
RUN rm /usr/lib/python3.*/EXTERNALLY-MANAGED &>/dev/null; \
    poetry install

CMD docker-files/$cmd_file


