from sqlalchemy import ForeignKey, String, text, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declarative_base, relationship
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    content: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="posts")
