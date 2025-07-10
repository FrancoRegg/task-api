from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import jwt
from jwt import PyJWTError
from app.core.config import settings
from app.schemas.token import TokenData

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow().replace(tzinfo=timezone.utc) + \
        timedelta(minutes=settings.access_token_expire_minutes)
    to_encode["exp"] = expire
    if "sub" not in to_encode:
        to_encode["sub"] = data.get("sub")
    # Use settings for key and algorithm
    token = jwt.encode(to_encode, settings.secret_key,
                       algorithm=settings.algorithm)
    return token


def verify_access_token(token: str) -> TokenData:
    try:
        payload = jwt.decode(token, settings.secret_key,
                             algorithms=[settings.algorithm])
        email = payload.get("sub")
        if not email:
            raise ValueError("Token inválido: no contiene sujeto")
        return TokenData(email=email)
    except PyJWTError as e:
        # Provide consistent exception type
        raise ValueError(f"Token inválido: {e}")
