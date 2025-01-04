from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud

from database import get_db
from schemas import (
    ConstructionObject,
    ConstructionObjectSimple,
    ConstructionObjectCreate,
    ConstructionObjectUpdate
)

router = APIRouter()

@router.get("/", response_model=List[ConstructionObjectSimple])
def get_all_objects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_construction_objects(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=ConstructionObjectSimple)
def get_object(id: int, db: Session = Depends(get_db)):
    obj = crud.get_construction_object(db, object_id=id)
    if not obj:
        raise HTTPException(status_code=404, detail="Object not found")
    return obj

@router.post("/", response_model=ConstructionObjectCreate)
def create_object(obj: ConstructionObjectCreate, db: Session = Depends(get_db)):
    return crud.create_construction_object(db, obj)

@router.patch("/{id}", response_model=ConstructionObjectUpdate)
def update_object(id: int, obj: ConstructionObjectUpdate, db: Session = Depends(get_db)):
    return crud.update_construction_object(db, object_id=id, object_data=obj)

@router.delete("/{id}", response_model=dict)
def delete_object(id: int, db: Session = Depends(get_db)):
    crud.delete_construction_object(db, object_id=id)
    return {"message": "Construction object deleted successfully"}
