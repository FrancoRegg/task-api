from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserOut
from app.crud.user import get_user_by_email, create_user
from app.api.deps import get_db
from app.utils.security import verify_password, create_access_token
from app.schemas.token import Token

router = APIRouter(tags=["auth"])


@router.post("/register",
             response_model=UserOut,
             status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    # 1) verificar si el e-mail ya existe
    existing = get_user_by_email(db, email=user_in.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email ya registrado"
        )

    # 2) crear usuario
    user = create_user(db, user_in)
    return user  # FastAPI + Pydantic lo serializan a UserOut


router = APIRouter(tags=["auth"])


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # 1) buscar usuario por email (= username)
    user = get_user_by_email(db, email=form_data.username)
    if not user:
        raise HTTPException(
            status_code=400, detail="Usuario o contraseña incorrectos")
    # 2) verificar password
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=400, detail="Usuario o contraseña incorrectos")
    # 3) generar token con "sub" = email
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
