from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

# 接続情報（docker-compose.ymlの設定と合わせる）
DB_CONFIG = {
    "host": "db", # サービス名がホスト名になる
    "database": "test_db",
    "user": "user",
    "password": "password",
}

@app.get("/")
def read_root():
    return {"message": "Hello PostgreSQL!"}

@app.get("/db-test")
def test_db_connection():
    try:
        # データベースに接続
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        # PostgreSQLのバージョンを取得するクエリを実行
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        
        cur.close()
        conn.close()
        
        return {"status": "success", "db_version": db_version[0]}
    except Exception as e:
        return {"status": "error", "message": str(e)}