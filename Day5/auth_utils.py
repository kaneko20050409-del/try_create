from passlib.context import CryptContext

# ハッシュ化のアルゴリズムとして bcrypt を指定
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """
    平文のパスワードをハッシュ化して返します。
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    平文のパスワードとハッシュ化されたパスワードが一致するか検証します。
    """
    return pwd_context.verify(plain_password, hashed_password)