from datetime import datetime

from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_user_id: Mapped[int] = mapped_column(unique=True)
    full_name: Mapped[str]

    shifts: Mapped[list["Shift"]] = relationship(back_populates="employee")


class Shift(Base):
    __tablename__ = "shifts"

    id: Mapped[int] = mapped_column(primary_key=True)
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"))
    starts_at: Mapped[datetime]
    ends_at: Mapped[datetime]

    employee: Mapped["Employee"] = relationship(back_populates="shifts")


class Dialog(Base):
    """Чернетка уточнення задачі з Gemini. Видаляється з чату після створення задачі в Vikunja."""

    __tablename__ = "dialogs"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_chat_id: Mapped[int]
    telegram_message_id: Mapped[int | None]
    status: Mapped[str] = mapped_column(default="new")  # new | clarifying | confirming | created
    collected_fields: Mapped[dict] = mapped_column(JSON, default=dict)
    vikunja_task_id: Mapped[int | None] = mapped_column(default=None)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
