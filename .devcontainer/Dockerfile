# 1. 土台となるPython環境（軽量版）
FROM python:3.12-slim

# 2. コンテナの中の作業場所を /app に決める
WORKDIR /app

# 3. ライブラリ一覧をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 今のフォルダのコードをすべてコンテナにコピー
COPY . .

# 5. UvicornでAPIを起動（0.0.0.0で待ち受けるのがコツ）
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]