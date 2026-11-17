from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .router.chat import chat, chat_stream
from fastapi_llm_demo.database.database import engine
from fastapi_llm_demo.database.collections import Base
from contextlib import asynccontextmanager

# from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动服务前，建表
    async with engine.begin() as conn:
        # 用 run_sync 包装同步的 create_all
        await conn.run_sync(Base.metadata.create_all)
    yield
    # 服务关闭，释放连接池
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

app.add_middleware(CORSMiddleware, allow_origins=["*"])

app.include_router(chat.router)
app.include_router(chat_stream.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}