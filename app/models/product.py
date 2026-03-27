from sqlalchemy import Column, Integer, String, Float
from app.db.database import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    stock = Column(Integer)
    price = Column(Float)