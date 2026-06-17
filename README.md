# Курск 1000 Backend
Установить зависимости:

```powershell
python -m pip install -r requirements.txt
```

Запустить API:

```powershell
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```


## API

### Проверка работы сервера

```http
GET /health
```

Ответ:

```json
{
  "status": "ok"
}
```

### Получить все достопримечательности

Этот эндпоинт нужен для кеширования.

```http
GET /landmarks
```

Пример ответа:

```json
[
  {
    "uuid": "A1B2C3D4-E5F6-7890-ABCD-EF1234567890",
    "name": "Знаменский собор",
    "emoji": "⛪️",
    "description": "...",
    "fact": "...",
    "year": "1816",
    "public_key": ""
  }
]
```

### Получить достопримечательность по UUID маяка

```http
GET /landmark/{uuid}
```

Пример:

```text
http://localhost:8000/landmark/A1B2C3D4-E5F6-7890-ABCD-EF1234567890
```

Ответ:

```json
{
  "uuid": "A1B2C3D4-E5F6-7890-ABCD-EF1234567890",
  "name": "Знаменский собор",
  "emoji": "⛪️",
  "description": "...",
  "fact": "...",
  "year": "1816",
  "public_key": ""
}
```

Если UUID не найден, сервер вернет `404`.