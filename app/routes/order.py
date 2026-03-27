from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.product import Product
from app.models.order import Order
from app.models.order_item import OrderItem
from app.schemas.order import OrderCreate
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/orders")
def create_order(order: OrderCreate, db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)):
    try:
        total = 0
        order_items = []

        for item in order.items:
            product = db.query(Product).filter(Product.id == item.product_id).first()

            if not product:
                raise HTTPException(status_code=404, detail="Product not found")

            if product.stock < item.quantity:
                raise HTTPException(status_code=400, detail="Not enough stock")

            product.stock -= item.quantity
            total += product.price * item.quantity

            order_items.append(item)

        new_order = Order(total=total)
        db.add(new_order)
        db.commit()
        db.refresh(new_order)

        for item in order_items:
            db_item = OrderItem(
                order_id=new_order.id,
                product_id=item.product_id,
                quantity=item.quantity
            )
            db.add(db_item)

        db.commit()

        return {"order_id": new_order.id, "total": total}

    except Exception as e:
        db.rollback()
        raise e