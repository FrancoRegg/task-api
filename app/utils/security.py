from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from app.schemas.token import TokenData
from app.core.config import Settings
from jwt import PyJWTError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(datetime.timezone.utc) + \
        timedelta(minutes=Settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, Settings.secret_key, algorithm=Settings.algorithm)
    return encoded_jwt


def verify_access_token(token: str) -> TokenData:
    try:
        payload = jwt.decode(token, Settings.secret_key,
                             algorithms=[Settings.algorithm])
        email: str = payload.get("sub")
        if email is None:
            raise ValueError("Token inválido: no contiene sujeto")
        return TokenData(email=email)
    except PyJWTError as e:
        raise ValueError(f"Token inválido: {e}")
