from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
# from sqlalchemy.orm import sessionmaker

db_url = "postgresql+asyncpg://postgres:seven9192@localhost:5432/llmDemo"
engine = create_async_engine(db_url)
# autoflush 查询操作前，是否自动把session中未提交的改动同步到数据库
session = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def get_db():
    db = session()
    try:
        yield db
    finally:
        await db.close()