from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# 向上3层定位到.env所在的根目录
BASE_DIR = Path(__file__).parent.parent.parent

class Settings(BaseSettings):
    DEEPSEEK_API_KEY: str
    DEEPSEEK_BASE_URL: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",  # 指定.env文件路径
        env_file_encoding="utf-8",
        extra="ignore" # 忽略未定义的环境变量，生产环境优先读系统环境变量
    )

settings = Settings()