from pydantic import BaseModel
from typing import List, Optional
from datetime import date

# -------------------- Base Models --------------------
# These are used for nested relationships to prevent circular references

class CustomerBase(BaseModel):
    name: str
    total_budget: Optional[float]
    additional_info: Optional[str]

class ConstructionObjectBase(BaseModel):
    name: str
    type: Optional[str]
    cost: Optional[float]
    start_date: Optional[date]
    end_date: Optional[date]
    customer_id: Optional[int]

class ContractorBase(BaseModel):
    name: str
    specialization: str
    num_employees: Optional[int]
    equipment_level: Optional[str]
    tools_level: Optional[str]

# -------------------- Simple Response Models --------------------
# These models don't include relationships

class CustomerSimple(CustomerBase):
    id: int

    class Config:
        from_attributes = True  # new name for orm_mode

class ConstructionObjectSimple(ConstructionObjectBase):
    id: int

    class Config:
        from_attributes = True

class ContractorSimple(ContractorBase):
    id: int

    class Config:
        from_attributes = True

# -------------------- Full Response Models --------------------
# These include relationships but use the Simple models to prevent circular references

class ConstructionObject(ConstructionObjectBase):
    id: int
    customer: Optional[CustomerSimple]
    contractors: List[ContractorSimple] = []

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

class Customer(CustomerBase):
    id: int
    construction_objects: List[ConstructionObjectSimple] = []

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

class Contractor(ContractorBase):
    id: int
    construction_objects: List[ConstructionObjectSimple] = []

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

# -------------------- Create/Update Models --------------------

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    total_budget: Optional[float] = None
    additional_info: Optional[str] = None

class ConstructionObjectCreate(ConstructionObjectBase):
    customer_id: int  # Make this required for creation

class ConstructionObjectUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    cost: Optional[float] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    customer_id: Optional[int] = None

class ContractorCreate(ContractorBase):
    pass

class ContractorUpdate(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    num_employees: Optional[int] = None
    equipment_level: Optional[str] = None
    tools_level: Optional[str] = None