from sqlalchemy import Boolean, create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine("postgresql://test_1:q1w2e3r4@admin/tododb")

Base = declarative_base()


class User(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    completed = Column(Boolean)
