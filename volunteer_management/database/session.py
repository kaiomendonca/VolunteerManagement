import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from volunteer_management.database.base import Base

DATABASE_URL = os.getenv("DATABASE_URL") or "sqlite:///./test.db"
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args=connect_args,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
