from sqlalchemy import Column, Table, Integer, String, Float, Date, Boolean, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import declarative_base

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

    # Новые колонки
    rating = Column(Float, nullable=True)
    is_active = Column(Boolean, default=True)

    # Индексы
    __table_args__ = (
        Index("ix_contractors_specialization", "specialization"),
    )

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
    end_date = Column(Date)  #

    # Новые колонки
    status = Column(String, default="In Progress")
    num_workers = Column(Integer, nullable=True)

    # Индексы
    __table_args__ = (
        Index("ix_construction_objects_status", "status"),
    )

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

    # Новые колонки
    vip_status = Column(Boolean, default=False)
    contact_email = Column(String, nullable=True)

    # Индексы
    __table_args__ = (
        Index("ix_customers_vip_status", "vip_status"),
    )

    construction_objects = relationship("ConstructionObject", back_populates="customer")
