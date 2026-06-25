from sqlalchemy import JSON, Column, String, Text

from .database import Base


class Landmark(Base):
    __tablename__ = "landmarks"

    uuid = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    subtitle = Column(String, nullable=False, default="")   # короткий подзаголовок под названием
    year = Column(String, nullable=False, default="")
    summary = Column(Text, nullable=False, default="")      # лид-абзац (виден сразу)
    cover_image = Column(String, nullable=False, default="")  # относительный путь к обложке
    sections = Column(JSON, nullable=False, default=list)   # [{"title": str, "body": str}]
    facts = Column(JSON, nullable=False, default=list)      # ["факт", ...]
    gallery = Column(JSON, nullable=False, default=list)    # [{"type": "image|video", "src": str, "caption": str}]
    beacon_secret = Column(String, nullable=False, default="")    # секрет метки для защиты от спуфинга.
