from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import String
from . import json_schemas, json_field_model
from fastapi import Query

from database import get_db

router = APIRouter()

@router.patch("/{id}/update_json", response_model=json_schemas.ContractorUpdate)
def update_json_field(
    id: int,
    json_data: dict,
    db: Session = Depends(get_db)
):
    contractor = db.query(json_field_model.Contractor).filter(json_field_model.Contractor.id == id).first()
    if not contractor:
        raise HTTPException(status_code=404, detail="Contractor not found")

    contractor.json_data = json_data
    db.commit()
    db.refresh(contractor)
    return contractor

@router.get("/search_by_json", response_model =json_schemas.ContractorResponse )
def search_by_json(
    pattern: str = Query(..., description="Регулярное выражение для поиска"),
    db: Session = Depends(get_db)
):
    contractors = db.query(json_field_model.Contractor).filter(
        json_field_model.Contractor.json_data.cast(String).op("~")(pattern)
    ).all()
    return contractors

@router.patch("/{id}/update_json", response_model=json_schemas.ConstructionObjectUpdate)
def update_json_field(
    id: int,
    json_data: dict,
    db: Session = Depends(get_db)
):
    construction_object = db.query(json_field_model.Contractor).filter(json_field_model.Contractor.id == id).first()
    if not construction_object:
        raise HTTPException(status_code=404, detail="Contractor not found")

    construction_object.json_data = json_data
    db.commit()
    db.refresh(construction_object)
    return construction_object

@router.get("/search_by_json", response_model =json_schemas.ConstructionObjectResponse )
def search_by_json(
    pattern: str = Query(..., description="Регулярное выражение для поиска"),
    db: Session = Depends(get_db)
):
    construction_objects = db.query(json_field_model.ConstructionObject).filter(
        json_field_model.ConstructionObject.json_data.cast(String).op("~")(pattern)
    ).all()

    return construction_objects

@router.patch("/{id}/update_json", response_model=json_schemas.CustomerUpdate)
def update_json_field(
    id: int,
    json_data: dict,
    db: Session = Depends(get_db)
):
    customer = db.query(json_field_model.Customer).filter(json_field_model.Contractor.id == id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    customer.json_data = json_data
    db.commit()
    db.refresh(customer)
    return customer

@router.get("/search_by_json", response_model =json_schemas.CustomerResponse )
def search_by_json(
    pattern: str = Query(..., description="Регулярное выражение для поиска"),
    db: Session = Depends(get_db)
):
    customers = db.query(json_field_model.Customer).filter(
        json_field_model.Customer.json_data.cast(String).op("~")(pattern)
    ).all()
    return customers


