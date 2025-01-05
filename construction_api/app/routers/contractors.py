from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

import crud, models

from database import get_db
from schemas import (
    Contractor,
    ContractorSimple,
    ContractorCreate,
    ContractorUpdate,
    LinkObject
)

router = APIRouter()

@router.get("/", response_model=List[ContractorSimple])
def get_all_contractors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_contractors(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=ContractorSimple)
def get_contractor(id: int, db: Session = Depends(get_db)):
    contractor = crud.get_contractor(db, contractor_id=id)
    if not contractor:
        raise HTTPException(status_code=404, detail="Contractor not found")
    return contractor

@router.post("/", response_model=Contractor)
def create_contractor(contractor: ContractorCreate, db: Session = Depends(get_db)):
    return crud.create_contractor(db, contractor)

@router.post("/{contractor_id}/link_object/", response_model=Contractor)
def link_object_to_contractor(
    contractor_id: int,
    object_data: LinkObject,
    db: Session = Depends(get_db),
):
    contractor = db.query(models.Contractor).filter(models.Contractor.id == contractor_id).first()
    if not contractor:
        raise HTTPException(status_code=404, detail="Contractor not found")

    construction_object = db.query(models.ConstructionObject).filter(
        models.ConstructionObject.id == object_data.object_id).first()
    if not construction_object:
        raise HTTPException(status_code=404, detail="ConstructionObject not found")

    contractor.construction_objects.append(construction_object)
    db.commit()
    db.refresh(contractor)

    return contractor

@router.patch("/{id}", response_model=ContractorUpdate)
def update_contractor(id: int, contractor: ContractorUpdate, db: Session = Depends(get_db)):
    return crud.update_contractor(db, contractor_id=id, contractor_data=contractor)

@router.delete("/{id}", response_model=dict)
def delete_contractor(id: int, db: Session = Depends(get_db)):
    crud.delete_contractor(db, contractor_id=id)
    return {"message": "Contractor deleted successfully"}
