import os
from dotenv import load_dotenv

# .envファイルをロード
load_dotenv()

class Settings:
    PROJECT_NAME: str = "FastAPI Project"
    VERSION: str = "1.0.0"

    # データベース設定
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

    # CORS設定
    ALLOWED_ORIGINS = ["*"]  # フロントエンドとAPIを接続する場合に適宜変更

    # JWT設定（認証を使う場合）
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_secret_key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
