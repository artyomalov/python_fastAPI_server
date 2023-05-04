from sqlalchemy import Table, Column, String, Boolean, Integer, MetaData

metadata = MetaData()

todos = Table(
    "todos",
    metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('text', String, nullable=False),
    Column('completed', Boolean)
)
