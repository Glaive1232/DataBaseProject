from sqlalchemy.orm import Session
import models, schemas

# Создание подрядчика
def create_contractor(db: Session, contractor_data: schemas.ContractorCreate):
    contractor = models.Contractor(**contractor_data.dict())
    db.add(contractor)
    db.commit()
    db.refresh(contractor)
    return contractor

# Получение всех подрядчиков
def get_contractors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Contractor).offset(skip).limit(limit).all()

# Получение подрядчика по ID
def get_contractor(db: Session, contractor_id: int):
    return db.query(models.Contractor).filter(models.Contractor.id == contractor_id).first()

# Обновление подрядчика
def update_contractor(db: Session, contractor_id: int, contractor_data: schemas.ContractorUpdate):
    contractor = db.query(models.Contractor).filter(models.Contractor.id == contractor_id).first()
    for key, value in contractor_data.dict(exclude_unset=True).items():
        setattr(contractor, key, value)
    db.commit()
    db.refresh(contractor)
    return contractor

# Удаление подрядчика
def delete_contractor(db: Session, contractor_id: int):
    contractor = db.query(models.Contractor).filter(models.Contractor.id == contractor_id).first()
    db.delete(contractor)
    db.commit()

# Создание объекта строительства
def create_construction_object(db: Session, object_data: schemas.ConstructionObjectCreate):
    obj = models.ConstructionObject(**object_data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# Получение всех объектов строительства
def get_construction_objects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ConstructionObject).offset(skip).limit(limit).all()

# Получение объекта по ID
def get_construction_object(db: Session, object_id: int):
    return db.query(models.ConstructionObject).filter(models.ConstructionObject.id == object_id).first()

# Обновление объекта строительства
def update_construction_object(db: Session, object_id: int, object_data: schemas.ConstructionObjectUpdate):
    obj = db.query(models.ConstructionObject).filter(models.ConstructionObject.id == object_id).first()
    for key, value in object_data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

# Удаление объекта строительства
def delete_construction_object(db: Session, object_id: int):
    obj = db.query(models.ConstructionObject).filter(models.ConstructionObject.id == object_id).first()
    db.delete(obj)
    db.commit()

# Создание заказчика
def create_customer(db: Session, customer_data: schemas.CustomerCreate):
    customer = models.Customer(**customer_data.dict())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

# Получение всех заказчиков
def get_customers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Customer).offset(skip).limit(limit).all()

# Получение заказчика по ID
def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

# Обновление заказчика
def update_customer(db: Session, customer_id: int, customer_data: schemas.CustomerUpdate):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    for key, value in customer_data.dict(exclude_unset=True).items():
        setattr(customer, key, value)
    db.commit()
    db.refresh(customer)
    return customer

# Удаление заказчика
def delete_customer(db: Session, customer_id: int):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    db.delete(customer)
    db.commit()
