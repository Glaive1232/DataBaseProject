from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

import crud

from database import get_db
from schemas import (
    Contractor,
    ContractorSimple,
    ContractorCreate,
    ContractorUpdate
)

router = APIRouter()

@router.get("/", response_model=List[ContractorSimple])
def get_all_contractors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_contractors(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=ContractorSimple)
def get_contractor(id: int, db: Session = Depends(get_db)):
    contractor = crud.et_contractor(db, contractor_id=id)
    if not contractor:
        raise HTTPException(status_code=404, detail="Contractor not found")
    return contractor

@router.post("/", response_model=ContractorCreate)
def create_contractor(contractor: ContractorCreate, db: Session = Depends(get_db)):
    return crud.create_contractor(db, contractor)

@router.patch("/{id}", response_model=ContractorUpdate)
def update_contractor(id: int, contractor: ContractorUpdate, db: Session = Depends(get_db)):
    return crud.update_contractor(db, contractor_id=id, contractor_data=contractor)

@router.delete("/{id}", response_model=dict)
def delete_contractor(id: int, db: Session = Depends(get_db)):
    crud.delete_contractor(db, contractor_id=id)
    return {"message": "Contractor deleted successfully"}
