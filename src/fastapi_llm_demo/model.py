from pydantic import BaseModel

class LLMReq(BaseModel):
    prompt: str
    model: str = "deepseek-flash"
    stream: bool = True
    thinking: bool = False