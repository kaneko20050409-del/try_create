from fastapi import APIRouter
from pydantic import BaseModel # これが必要！

router = APIRouter(prefix="/users", tags=["users"])

# 1. 送られてくるデータの「形」をクラスで定義（モデル）
class UserCreate(BaseModel):
    name: str
    age: int
    email: str

# 簡易的なデータベース（リスト）
fake_users_db = []

# 2. @router.post を使う
@router.post("/register")
def create_user(user: UserCreate):
    # user は UserCreate クラスのインスタンスとして届く
    fake_users_db.append(user)
    return {"message": "登録完了！", "data": user}