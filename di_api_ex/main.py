from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime

app = FastAPI()

# 擬似的なDB接続クラス（本来はSQLAlchemyなどを使います）
class DBSession:
    def close(self):
        print("DB接続を閉じました")

# 1. 依存関係となる関数（スタッフの動き）
def get_db():
    db = DBSession() # 準備：DBに繋ぐ
    try:
        yield db     # 道具を渡す（ここでエンドポイントの処理にバトンタッチ）
    finally:
        db.close()   # 後片付け：終わったら必ず閉じる

class PostCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1)

class PostResponse(PostCreate):
    id: int
    created_at: datetime
    # 内部管理用のフラグなどはここには書かない（＝ユーザーに返さない）

@app.post("/posts/")
async def create_post(post: PostCreate, db: DBSession = Depends(get_db)):
    # 関数が始まる前に get_db が動いて db を用意してくれる
    print(f"DBを使って {post.title} を保存中...")
    
    # ここが終わると、自動的に get_db の finally 以降が実行される
    return {"status": "success"}