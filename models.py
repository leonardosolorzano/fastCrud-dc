from __future__ import annotations

from datetime import UTC, datetime
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    image_file: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
        default=None,
    )

    posts: Mapped[list["Post"]] = relationship(back_populates="author") # Relación con la tabla Post

    @property # Nos permite acceder a la propiedad como si fuera un atributo
    def image_path(self) -> str:
        if self.image_file:
            return f"/static/profile_pics/{self.image_file}"
        return "/static/profile_pics/default.jpg"

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    content: Mapped[str] = mapped_column(Text)
    date_posted: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )
    
    author: Mapped["User"] = relationship(back_populates="posts")
    
