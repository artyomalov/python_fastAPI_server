"""Get db object, get engine object
    """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
BASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(BASE_URL, connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

