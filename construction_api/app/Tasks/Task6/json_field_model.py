from sqlalchemy import Column, Table, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()

# Ассоциативная таблица для связи "многие ко многим" между Подрядчиком и Объектом
contractor_object_association = Table(
    "contractor_object_association",
    Base.metadata,
    Column("contractor_id", Integer, ForeignKey("contractors.id"), primary_key=True),
    Column("object_id", Integer, ForeignKey("construction_objects.id"), primary_key=True),
)

# Модель для подрядчиков
class Contractor(Base):
    __tablename__ = "contractors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    specialization = Column(String, nullable=False)
    num_employees = Column(Integer)
    equipment_level = Column(String)
    tools_level = Column(String)

    json_data = Column(JSONB, nullable=True)


    construction_objects = relationship(
        "ConstructionObject",
        secondary=contractor_object_association,
        back_populates="contractors"
    )

# Модель для объектов строительства
class ConstructionObject(Base):
    __tablename__ = "construction_objects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    type = Column(String)
    cost = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date)

    json_data = Column(JSONB, nullable=True)

    contractors = relationship(
        "Contractor",
        secondary=contractor_object_association,
        back_populates="construction_objects"
    )

    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="construction_objects")


# Модель для заказчиков
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    total_budget = Column(Float)
    additional_info = Column(String)

    json_data = Column(JSONB, nullable=True)

    construction_objects = relationship("ConstructionObject", back_populates="customer")
