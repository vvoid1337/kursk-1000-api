from pydantic import BaseModel


class LandmarkResponse(BaseModel):
    uuid: str
    name: str
    emoji: str
    description: str
    fact: str
    year: str
    public_key: str = ""
