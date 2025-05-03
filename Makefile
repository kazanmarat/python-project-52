dev:
	uv run manage.py runserver

build:
	./build.sh

install:
	uv sync

collectstatic:
	uv run manage.py collectstatic

migrate:
	uv run manage.py migrate

render-start:
	gunicorn task_manager.wsgi

compile:
	uv pip compile pyproject.toml -o requirements.txt

i18n-ru:
	uv run manage.py makemessages -l ru

i18n-compile:
	uv run manage.py compilemessages
