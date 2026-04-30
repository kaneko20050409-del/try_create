from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

app = FastAPI()

class PostCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1)

class PostResponse(PostCreate):
    id: int
    created_at: datetime
    # 内部管理用のフラグなどはここには書かない（＝ユーザーに返さない）

# 擬似データベース（実際はDBから取得したデータを想定）
fake_db = []

@app.post("/posts/", response_model=PostResponse, status_code=201)
async def create_post(post: PostCreate):
    # 実際はここでDB保存処理
    new_post_data = {
        "id": len(fake_db) + 1,
        "title": post.title,
        "content": post.content,
        "created_at": datetime.now(),
        "internal_memo": "これは管理用なのでレスポンスには含めない"
    }
    fake_db.append(new_post_data)
    
    # response_model=PostResponse を指定しているので、
    # new_post_data の中から PostResponse にある項目だけが抽出されて返される
    return new_post_data