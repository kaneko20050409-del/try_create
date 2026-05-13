from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

# 共通のバリデーション
class UserBase(BaseModel):
    username: str
    email: EmailStr

# 作成時のリクエスト用
class UserCreate(UserBase):
    password: str = Field(..., max_length=72)  # DB保存前にハッシュ化するのが一般的

# 取得時のレスポンス用
class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True # SQLAlchemyモデルをPydanticに変換可能にする