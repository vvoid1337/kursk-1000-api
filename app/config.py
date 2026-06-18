import os

# в бд хранятся относительные пути для медиа.
# переезд на собственный CDN = смена одной этой переменной окружения.
MEDIA_BASE_URL = os.getenv(
    "MEDIA_BASE_URL",
    "https://raw.githubusercontent.com/vvoid1337/kursk-1000-api/master/media",
).rstrip("/")


def media_url(path: str | None) -> str | None:
    """Собрать абсолютный URL медиа из относительного пути.

    Если в БД уже лежит абсолютная ссылка (http/https) — возвращаем как есть,
    что позволяет при необходимости переопределять источник по конкретной записи.
    """
    if not path:
        return None
    if path.startswith(("http://", "https://")):
        return path
    return f"{MEDIA_BASE_URL}/{path.lstrip('/')}"
