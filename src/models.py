from pydantic import BaseModel

class CodeRequest(BaseModel):
    prompt: str
    language: str = "Python"
    max_length: int = 256

class CodeResponse(BaseModel):
    generated_code: str
