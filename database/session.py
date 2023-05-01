"""Get db object, get engine object
    """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from basemodel import Todo
BASE_URL = "sqlite:///./sql_app.db"
# "postgresql://postgres:admin@localhost:5432/todos"

engine = create_engine(BASE_URL, connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()


#  через sessionLocal можно создать объект этого класс и через него работать с бд
# \conninfo
