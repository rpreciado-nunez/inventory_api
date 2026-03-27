from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    stock: int
    price: float