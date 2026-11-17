from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .router.chat import chat, chat_stream

# from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])

app.include_router(chat.router)
app.include_router(chat_stream.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}