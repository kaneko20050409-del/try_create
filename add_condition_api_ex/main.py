from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, constr, field_validator
from typing import Optional

app = FastAPI()

# 1. リクエストを受け取るためのスキーマ（バリデーションの定義）
class PostCreate(BaseModel):
    # min_length=1 で空文字を禁止、max_length で長すぎる入力を制限
    title: str = Field(..., min_length=1, max_length=100, description="記事のタイトル")

    @field_validator('title')
    @classmethod
    def check_bad_words(cls, v: str):
        if 'バカ' in v:
            raise ValueError('不適切な用語が含まれています。')
        return v

    content: str = Field(..., min_length=1, max_length=1000, description="記事の本文")
    published: bool = True

# 擬似的なデータベース
db = []

@app.post("/posts/", status_code=201)
async def create_post(post: PostCreate):
    # ここに到達した時点で、postの内容はすでにバリデーション済み
    new_post = post.model_dump()
    db.append(new_post)
    return new_post