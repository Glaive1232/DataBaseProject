from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
import crud, schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.Customer])
def get_all_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_customers(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.Customer)
def get_customer(id: int, db: Session = Depends(get_db)):
    customer = crud.get_customer(db, customer_id=id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.post("/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)

@router.patch("/{id}", response_model=schemas.Customer)
def update_customer(id: int, customer: schemas.CustomerUpdate, db: Session = Depends(get_db)):
    return crud.update_customer(db, customer_id=id, customer_data=customer)

@router.delete("/{id}", response_model=dict)
def delete_customer(id: int, db: Session = Depends(get_db)):
    crud.delete_customer(db, customer_id=id)
    return {"message": "Customer deleted successfully"}
