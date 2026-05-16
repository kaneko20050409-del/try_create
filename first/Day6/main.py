from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database
from auth_utils import get_password_hash # 前のステップで作ったハッシュ化関数

app = FastAPI()

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # 既存のユーザーチェック
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pw = get_password_hash(user.password) # user.password は生パスワード

    # 3. 【修正】ハッシュ化したパスワードをモデルに渡す
    new_user = models.User(
        username=user.username, 
        email=user.email,
        hashed_password=hashed_pw  # models.Userにこのカラムがある前提
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user) # IDなどの自動生成項目を反映
    return new_user

@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user