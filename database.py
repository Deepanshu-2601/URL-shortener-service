import os
os.environ["DISABLE_SQLALCHEMY_CEXT"] = "1"

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Local SQLite database file create hogi
SQLALCHEMY_DATABASE_URL = "sqlite:///./url_shortener.db"

# connect_args SQLite ke thread check ke liye zaroori hota hai
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# FastAPI endpoints ke liye DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()