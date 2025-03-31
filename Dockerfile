# Pythonの公式イメージをベースに使用
FROM python:3.10-slim

# 作業ディレクトリを作成
WORKDIR /app

# 必要な依存関係をコピーする
COPY requirements.txt .

# 必要なPythonライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY . .


# SQLite用のデータベースの初期化とシードデータ挿入
# RUN python seed.py

# FastAPIのサーバーを起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# コンテナが待機するポートを公開
EXPOSE 8000
