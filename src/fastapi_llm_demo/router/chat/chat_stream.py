from openai import AsyncOpenAI
from fastapi import APIRouter
from fastapi_llm_demo.config import settings
from fastapi.responses import StreamingResponse
from fastapi_llm_demo.model import LLMReq
import json

client = AsyncOpenAI(
    api_key=settings.DEEPSEEK_API_KEY,
    base_url=settings.DEEPSEEK_BASE_URL
)

router = APIRouter(
    prefix="/api",
    tags=["chat"],
    responses={404: {"description": "Not found"}}
)

async def generate_stream(response):
    async for chunk in response:
        delta = chunk.choices[0].delta
        # print(chunk)
        # print(delta)
        data = {}
        if delta.content:
            data["content"] = delta.content
        yield f"data: {json.dumps(data)}\n\n"

@router.post("/chat-stream")
async def chat_stream(req: LLMReq):
    extra_body = {}
    if req.thinking:
        extra_body["thinking"] = { "type": "enabled" }
    messages = [{"role": "user", "content": req.prompt}]
    response = await client.chat.completions.create(
        messages=messages,
        model=req.model,
        stream=req.stream,
        extra_body=extra_body
    )
    return StreamingResponse(
        generate_stream(response),
        media_type="text/event-stream"
    )
