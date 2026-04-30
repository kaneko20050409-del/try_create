from fastapi import APIRouter

router = APIRouter(prefix='/items', tags=['items'])

fake_items_db = {
    1: ["Python本", "MacBook", "コーヒーカップ"],
    2: ["スニーカー", "プロテイン"]
}

@router.get("/owner/{user_id}")
def get_items_by_user(user_id: int):
    # 特定のユーザーの持ち物を探して返す
    items = fake_items_db.get(user_id, [])
    return {"user_id": user_id, "owned_items": items}