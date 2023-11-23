from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# User schemas
class UserBase(BaseModel):
    login: str


class UserCreate(UserBase):
    first_name: str
    last_name: str
    email: str


class UserResponse(UserBase):
    id: int
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True


# Service schemas
class ServiceBase(BaseModel):
    name: str


class ServiceCreate(ServiceBase):
    description: str
    cost: float


class ServiceResponse(ServiceBase):
    id: int
    description: str
    cost: float

    class Config:
        orm_mode = True


class OrderServiceAdd(BaseModel):
    service_id: int


# Order schemas
class OrderBase(BaseModel):
    user_id: int
    service_ids: List[int]
    date_created: datetime


class OrderCreate(BaseModel):
    user_id: int
    service_ids: List[int]


class OrderResponse(BaseModel):
    id: int
    user_id: int
    service_ids: List[int]
    date_created: datetime

    class Config:
        orm_mode = True
