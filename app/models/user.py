from sqlalchemy import Column, Integer, String, DateTime
from app.models import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), nullable=False, unique=True, index=True)
    hashed_password = Column(String(120), nullable=False)
    created_at = Column(DateTime(timezone=True))
