from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserOut
from app.crud.user import get_user_by_email, create_user
from app.api.deps import get_db


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
