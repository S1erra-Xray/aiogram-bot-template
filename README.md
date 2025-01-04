# aiogram-bot-template

Template for creating scalable bots with aiogram

# Start develop

Before starting your own project, init it

```shell
poetry run python infra/scripts/init_project.py
```

# Using linters and static code analyzers

If you want to use formatters or code analyzers such as **black** or mypy, install it manualy by pip in system-wide
python interpreter and configure your IDE for its usage.

**ADVICE**: dont install linters and static code analyzers into docker, because it decreases performance