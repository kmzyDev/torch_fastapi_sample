from pydantic import BaseModel

class InputParams(BaseModel):
    prompt: str
