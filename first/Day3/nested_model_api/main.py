from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# 1. 小さな部品：タグモデル
class Tag(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=20)

# 2. 大きな部品：商品モデル（Tagを中で使っている）
class Item(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    
    # ここがポイント！作成したTagモデルを型として指定
    # 単一のタグなら「tag: Tag」、複数のタグなら「tags: List[Tag]」
    tags: List[Tag] = Field(default=[], description="商品に関連付けられたタグのリスト")

@app.post("/items/nested")
async def create_nested_item(item: Item):
    # ネストされたデータもそのままPythonオブジェクトとして扱えます
    tag_count = len(item.tags)
    
    return {
        "message": f"{tag_count}個のタグを含む商品を登録しました",
        "item_data": item
    }