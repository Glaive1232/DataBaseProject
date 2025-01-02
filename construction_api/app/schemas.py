from pydantic import BaseModel
from typing import List, Optional
from datetime import date


# -------------------- Contractor --------------------

# Схема для создания подрядчика
class ContractorCreate(BaseModel):
    name: str
    specialization: str
    num_employees: Optional[int]
    equipment_level: Optional[str]
    tools_level: Optional[str]


# Схема для обновления подрядчика
class ContractorUpdate(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    num_employees: Optional[int] = None
    equipment_level: Optional[str] = None
    tools_level: Optional[str] = None


# Схема для отображения подрядчика
class Contractor(BaseModel):
    id: int
    name: str
    specialization: str
    num_employees: Optional[int]
    equipment_level: Optional[str]
    tools_level: Optional[str]
    # Связь с объектами
    construction_objects: List["ConstructionObject"] = []

    class Config:
        orm_mode = True


# -------------------- ConstructionObject --------------------

# Схема для создания объекта строительства
class ConstructionObjectCreate(BaseModel):
    name: str
    type: Optional[str]
    cost: Optional[float]
    start_date: Optional[date]
    end_date: Optional[date]
    customer_id: int  # ID заказчика


# Схема для обновления объекта строительства
class ConstructionObjectUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    cost: Optional[float] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    customer_id: Optional[int] = None


# Схема для отображения объекта строительства
class ConstructionObject(BaseModel):
    id: int
    name: str
    type: Optional[str]
    cost: Optional[float]
    start_date: Optional[date]
    end_date: Optional[date]
    customer_id: Optional[int]
    # Связи
    customer: Optional["Customer"]
    contractors: List[Contractor] = []

    class Config:
        orm_mode = True


# -------------------- Customer --------------------

# Схема для создания заказчика
class CustomerCreate(BaseModel):
    name: str
    total_budget: Optional[float]
    additional_info: Optional[str]


# Схема для обновления заказчика
class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    total_budget: Optional[float] = None
    additional_info: Optional[str] = None


# Схема для отображения заказчика
class Customer(BaseModel):
    id: int
    name: str
    total_budget: Optional[float]
    additional_info: Optional[str]
    # Связь с объектами
    construction_objects: List[ConstructionObject] = []

    class Config:
        orm_mode = True
