from sqlalchemy.orm import Session
import models, schemas

def create_contractor(db: Session, contractor_data: schemas.ContractorCreate):
    contractor = models.Contractor(**contractor_data.dict())
    db.add(contractor)
    db.commit()
    db.refresh(contractor)
    return contractor

def get_contractors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Contractor).offset(skip).limit(limit).all()

def get_contractor(db: Session, contractor_id: int):
    return db.query(models.Contractor).filter(models.Contractor.id == contractor_id).first()

def update_contractor(db: Session, contractor_id: int, contractor_data: schemas.ContractorUpdate):
    contractor = db.query(models.Contractor).filter(models.Contractor.id == contractor_id).first()
    for key, value in contractor_data.dict(exclude_unset=True).items():
        setattr(contractor, key, value)
    db.commit()
    db.refresh(contractor)
    return contractor

def delete_contractor(db: Session, contractor_id: int):
    contractor = db.query(models.Contractor).filter(models.Contractor.id == contractor_id).first()
    db.delete(contractor)
    db.commit()