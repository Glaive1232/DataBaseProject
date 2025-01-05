from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import asc, desc

import crud, models
from database import get_db
from schemas import (
    Contractor,
    ContractorUpdate,
    LinkObject,
)

router = APIRouter()

# 1. Получить подрядчиков с определённой специализацией
@router.get("/by-specialization/", response_model=List[Contractor])
def get_contractors_by_specialization(
    specialization: str = Query(..., description="Специализация подрядчика"),
    db: Session = Depends(get_db)
):
    contractors = db.query(models.Contractor).filter(models.Contractor.specialization == specialization).all()
    if not contractors:
        raise HTTPException(status_code=404, detail="No contractors found with this specialization")
    return contractors

# 2. Получить подрядчиков и их объекты строительства
@router.get("/with-objects/", response_model=List[dict])
def get_contractors_with_objects(db: Session = Depends(get_db)):
    try:
        results = db.query(models.Contractor).all()
        data = [
            {
                "contractor_name": contractor.name,
                "specialization": contractor.specialization,
                "objects": [
                    {"object_name": obj.name, "type": obj.type, "cost": obj.cost}
                    for obj in contractor.construction_objects
                ]
            }
            for contractor in results
        ]
        return data

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

# 3. Обновить статус объекта строительства
@router.put("/construction-objects/{object_id}/status/")
def update_construction_object_status(
    object_id: int,
    status: str = Query(..., description="Новый статус объекта"),
    db: Session = Depends(get_db)
):
    construction_object = db.query(models.ConstructionObject).filter(models.ConstructionObject.id == object_id).first()
    if not construction_object:
        raise HTTPException(status_code=404, detail="Construction object not found")

    construction_object.status = status
    db.commit()
    db.refresh(construction_object)
    return {"message": f"Status of object '{construction_object.name}' updated to '{status}'"}

# 4. Группировать объекты строительства по типу
@router.get("/construction-objects/group-by-type/")
def group_objects_by_type(db: Session = Depends(get_db)):
    try:
        results = db.execute(
            """
            SELECT type, COUNT(*) AS object_count
            FROM construction_objects
            GROUP BY type;
            """
            
        )
        grouped_data = [{"type": row.type, "object_count": row.object_count} for row in results]
        return grouped_data

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

# 5. Rest Api запрос с сортировкой

@router.get("/sorted_contractors/", response_model=List[Contractor])
def get_sorted_contractors(
    sort_by: str = Query(
        "name",
        description="Поле для сортировки (например, 'name', 'specialization', 'num_employees')"
    ),
    order: str = Query(
        "asc",
        description="Направление сортировки ('asc' для по возрастанию, 'desc' для по убыванию)"
    ),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):

    valid_sort_fields = ["name", "specialization", "num_employees", "equipment_level", "tools_level"]
    if sort_by not in valid_sort_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort_by field. Valid options are: {', '.join(valid_sort_fields)}"
        )

    sort_order = asc if order == "asc" else desc
    try:
        contractors = (
            db.query(models.Contractor)
            .order_by(sort_order(getattr(models.Contractor, sort_by)))
            .offset(skip)
            .limit(limit)
            .all()
        )
        return contractors
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
