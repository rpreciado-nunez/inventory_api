from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg://inv_user:welcome123@localhost:5432/inventory_db"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "options": "-c client_encoding=utf8"
    }
)

SessionLocal = sessionmaker(bind=engine)