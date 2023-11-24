from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..models import Order, Service
from ..schemas import OrderCreate, OrderResponse, OrderServiceAdd
from ..database import get_db

router = APIRouter()


@router.post("/orders/", response_model=OrderResponse)
def create_order(order_create: OrderCreate, db: Session = Depends(get_db)):
    # Create a new Order instance
    new_order = Order(user_id=order_create.user_id)

    # Check and add services to the order
    for service_id in order_create.service_ids:
        service = db.query(Service).filter(Service.id == service_id).first()
        if not service:
            raise HTTPException(
                status_code=404, detail=f"Service with ID {service_id} not found"
            )
        new_order.services.append(service)

    # Add and commit the new order to the database
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

    added_services = []
    for service_id in service_data.service_ids:
        # Get each service from the database
        service = db.query(Service).filter(Service.id == service_id).first()
        if not service:
            raise HTTPException(
                status_code=404, detail=f"Service ID {service_id} not found"
            )

        # Add the service to the order if not already added
        if service not in order.services:
            order.services.append(service)
            added_services.append(service_id)

    # Commit changes if any new services were added
    if added_services:
        db.commit()
        db.refresh(order)
    else:
        raise HTTPException(
            status_code=400,
            detail="No new services added, all services already exist in the order",
        )

    return order
