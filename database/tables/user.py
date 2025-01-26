from sqlalchemy import create_engine, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.main import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)

    def __repr__(self):
        return f"<User({self.id=}, {self.name=}, {self.lastname=})>"
