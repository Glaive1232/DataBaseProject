from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud

from database import get_db
from schemas import (
    Customer,
    CustomerSimple,
    CustomerCreate,
    CustomerUpdate
)

router = APIRouter()

@router.get("/", response_model=List[CustomerSimple])
def get_all_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_customers(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=CustomerSimple)
def get_customer(id: int, db: Session = Depends(get_db)):
    customer = crud.get_customer(db, customer_id=id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.post("/", response_model=Customer)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)

@router.patch("/{id}", response_model=CustomerUpdate)
def update_customer(id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    return crud.update_customer(db, customer_id=id, customer_data=customer)

@router.delete("/{id}", response_model=dict)
def delete_customer(id: int, db: Session = Depends(get_db)):
    crud.delete_customer(db, customer_id=id)
    return {"message": "Customer deleted successfully"}
