from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import Service
from ..schemas import ServiceCreate, ServiceResponse
from ..database import get_db

router = APIRouter()


@router.post("/services/", response_model=ServiceResponse)
def create_service(service_create: ServiceCreate, db: Session = Depends(get_db)):
    # This endpoint will create a service with the given name, description, and cost
    new_service = Service(
        name=service_create.name,
        description=service_create.description,
        cost=service_create.cost,
    )
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service


@router.get("/services/", response_model=list[ServiceResponse])
def get_services(db: Session = Depends(get_db)):
    # This endpoint will retrieve all services
    services = db.query(Service).all()
    return services
