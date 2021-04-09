from pydantic import BaseModel


class ShortLink(BaseModel):
    short_url: str

    class Config:
        orm_mode = True
