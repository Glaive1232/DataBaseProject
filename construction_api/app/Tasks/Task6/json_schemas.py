from pydantic import BaseModel
from typing import Optional, Dict,Any
from datetime import date

class ContractorResponse(BaseModel):
    id: int
    name: Optional[str]
    specialization: Optional[str]
    num_employees: Optional[int]
    equipment_level: Optional[str]
    tools_level: Optional[str]
    json_data: Optional[Any]

    class Config:
        from_attributes = True

class ConstructionObjectResponse(BaseModel):
    id: int
    name: Optional[str]
    type: Optional[str]
    cost: Optional[float]
    start_date: Optional[date]
    end_date: Optional[date]
    customer_id: Optional[int]
    json_data: Optional[Any]

    class Config:
        from_attributes = True

class CustomerResponse(BaseModel):
    id: int
    name: Optional[str]
    total_budget: Optional[float]
    additional_info: Optional[str]
    json_data: Optional[Any]

    class Config:
        from_attributes = True
class ContractorUpdate(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    num_employees: Optional[int] = None
    equipment_level: Optional[str] = None
    tools_level: Optional[str] = None
    json_data: Optional[Dict] = None


class ConstructionObjectUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    cost: Optional[float] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    customer_id: Optional[int] = None


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    total_budget: Optional[float] = None
    additional_info: Optional[str] = None