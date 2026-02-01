up:
	docker compose up -d db

down:
	docker compose down

reset-db:
	docker compose down -v
	docker compose up -d db

migrate:
	ENV_FILE=.env.local poetry run alembic upgrade head

run:
	ENV_FILE=.env.local poetry run uvicorn src.main:app --reload

test:
	ENV_FILE=.env.test poetry run pytest -q
