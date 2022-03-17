from pydantic import BaseModel


class RovPosition(BaseModel):
    pen_id: str
    heading: float
    depth: float
    datetime: str
    status: str