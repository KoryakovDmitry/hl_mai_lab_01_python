from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import Order, Service
from ..schemas import OrderCreate, OrderResponse, OrderServiceAdd
from ..database import get_db

router = APIRouter()


@router.post("/orders/", response_model=OrderResponse)
def create_order(order_create: OrderCreate, db: Session = Depends(get_db)):
    # This endpoint will create an order with the given user_id and service_ids
    new_order = Order(
        user_id=order_create.user_id,
        service_ids=order_create.service_ids,
        date=order_create.date_created,
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


@router.get("/orders/{user_id}", response_model=list[OrderResponse])
def get_user_orders(user_id: int, db: Session = Depends(get_db)):
    # This endpoint will retrieve all orders for a given user_id
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    if not orders:
        raise HTTPException(status_code=404, detail="Orders not found for the user")
    return orders


@router.post("/orders/{order_id}/add_service", response_model=OrderResponse)
def add_service_to_order(
    order_id: int, service_data: OrderServiceAdd, db: Session = Depends(get_db)
):
    # Get the order from the database
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    # Get the service from the database
    service = db.query(Service).filter(Service.id == service_data.service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    # Add the service to the order
    if service not in order.services:
        order.services.append(service)
        db.commit()
        db.refresh(order)
        return order
    else:
        raise HTTPException(
            status_code=400, detail="Service already added to the order"
        )
