from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# 1. Pydanticモデルの定義
class Item(BaseModel):
    # 文字列の長さ制限 (1文字以上、50文字以内)
    name: str = Field(..., min_length=1, max_length=50, examples=["ゲーミングマウス"])
    
    # 数値の範囲制限 (0より大きいこと)
    price: float = Field(..., gt=0, description="価格は0より大きい必要があります")
    
    # 任意項目（デフォルト値あり）
    description: Optional[str] = Field(None, max_length=200)
    
    # リスト型
    tags: List[str] = []

# 2. POSTエンドポイントの作成
@app.post("/items/")
async def create_item(item: Item):
    # 中身を加工（例：税込価格を追加して返す）
    item_dict = item.model_dump() # Pydantic v2の書き方 (v1なら .dict())
    item_dict.update({"price_with_tax": item.price * 1.1})
    
    return {
        "message": "アイテムを登録しました",
        "data": item_dict
    }