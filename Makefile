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

start:
	uv run gunicorn task_manager.wsgi

render-start:
	gunicorn task_manager.wsgi

check: test lint

lint:
	uv run ruff check	

test-coverage:
	uv run coverage run --source='.' manage.py test
	uv run coverage xml

test:
	uv run manage.py test

test-accounts:
	uv run manage.py test accounts

test-statuses:
	uv run manage.py test statuses

test-tasks:
	uv run manage.py test tasks

test-labels:
	uv run manage.py test labels

i18n-ru:
	uv run manage.py makemessages -l ru

i18n-compile:
	uv run manage.py compilemessages
