from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, MetaData


Base = declarative_base()
metadata = MetaData()

class Todo(Base):
    __tablename__ = "todos"

    metadata
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    completed = Column(Boolean)
