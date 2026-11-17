from fastapi import APIRouter
from fastapi_llm_demo.config import settings # 导入env配置
from openai import AsyncOpenAI
from fastapi_llm_demo.model import LLMReq

# AsyncOpenAI才返回协程，可以加await，否则返回ChatCompletion对象
client = AsyncOpenAI(
    api_key=settings.DEEPSEEK_API_KEY,
    base_url=settings.DEEPSEEK_BASE_URL
)

router = APIRouter(
    prefix="/api", # 路由前缀
    tags=["chat"], # 文档分组标签
    responses={404: {"description": "Not found"}}
)

@router.post("/chat")
async def chat(req: LLMReq):
    extra_body = {}
    if req.thinking:
        extra_body["thinking"] = { "type": "enabled" }

    messages = [{"role": "user", "content": req.prompt}]
    response = await client.chat.completions.create(
        messages=messages,
        model=req.model,
        stream=False,
        extra_body=extra_body
    )
    return response