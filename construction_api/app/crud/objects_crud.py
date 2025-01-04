from sqlalchemy.orm import Session
import models, schemas

def create_construction_object(db: Session, object_data: schemas.ConstructionObjectCreate):
    obj = models.ConstructionObject(**object_data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_construction_objects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ConstructionObject).offset(skip).limit(limit).all()

def get_construction_object(db: Session, object_id: int):
    return db.query(models.ConstructionObject).filter(models.ConstructionObject.id == object_id).first()

def update_construction_object(db: Session, object_id: int, object_data: schemas.ConstructionObjectUpdate):
    obj = db.query(models.ConstructionObject).filter(models.ConstructionObject.id == object_id).first()
    for key, value in object_data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_construction_object(db: Session, object_id: int):
    obj = db.query(models.ConstructionObject).filter(models.ConstructionObject.id == object_id).first()
    db.delete(obj)
    db.commit()