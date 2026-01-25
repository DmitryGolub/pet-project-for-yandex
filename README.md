## Примеры параметров в .env
```
SECRET_KEY=secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXP_MINUTES=60

USERNAME=admin
PASSWORD=admin1234
```

## Устанавливаем зависимости
```aiignore
poetry install
```

## Запускаем проект
```aiignore
poetry run uvicorn src.main:app --reload
```