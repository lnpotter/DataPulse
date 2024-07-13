from pydantic import BaseModel

class DataPoint(BaseModel):
    value: float
    label: str
