from fastapi import FastAPI
from app.models.product import Base
from app.models import  order, order_item,user
from app.db.database import engine
from app.routes import product,order,user

# 1. Crear app PRIMERO
app = FastAPI()

# 2. Registrar rutas
app.include_router(product.router)
app.include_router(order.router)
app.include_router(user.router)

# 3. Crear tablas DESPUÉS
Base.metadata.create_all(bind=engine)

# 4. Endpoint base
@app.get("/")
def root():
    return {"message": "API running 🚀"}