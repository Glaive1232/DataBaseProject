from sqlalchemy import Column, Table, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from construction_api.app.database import Base

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
    name = Column(String, index=True, nullable=False)  # Название
    specialization = Column(String, nullable=False)  # Специализация
    num_employees = Column(Integer)  # Количество человек
    equipment_level = Column(String)  # Обеспеченность техникой
    tools_level = Column(String)  # Обеспеченность инструментом

    # Связь "многие ко многим" с объектами
    construction_objects = relationship(
        "ConstructionObject",
        secondary=contractor_object_association,
        back_populates="contractors"
    )

# Модель для объектов строительства
class ConstructionObject(Base):
    __tablename__ = "construction_objects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)  # Название объекта
    type = Column(String)  # Тип объекта
    cost = Column(Float)  # Стоимость
    start_date = Column(Date)  # Дата начала
    end_date = Column(Date)  # Дата конца

    # Связь "многие ко многим" с подрядчиками
    contractors = relationship(
        "Contractor",
        secondary=contractor_object_association,
        back_populates="construction_objects"
    )

    # Связь "многие к одному" с заказчиком
    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="construction_objects")


# Модель для заказчиков
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)  # Название заказчика
    total_budget = Column(Float)  # Сумма на счёте
    additional_info = Column(String)  # Информация о заказчике

    # Связь "один ко многим" с объектами
    construction_objects = relationship("ConstructionObject", back_populates="customer")
