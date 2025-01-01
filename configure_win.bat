set PROJECT_DIR=.

poetry run python -m ruff check %PROJECT_DIR% --config pyproject.toml --fix
poetry run python -m isort %PROJECT_DIR%
poetry run python -m mypy %PROJECT_DIR% --config-file pyproject.toml
poetry run python -m black %PROJECT_DIR% --config pyproject.toml

poetry run python infra/scripts/init_project.py