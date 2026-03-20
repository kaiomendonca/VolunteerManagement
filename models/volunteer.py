# models/volunteer.py
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import declarative_base
import enum

Base = declarative_base()

class AvailabilityEnum(enum.Enum):
    morning = "Morning"
    afternoon = "Afternoon"
    evening = "Evening"
    weekend = "Weekend"

class StatusEnum(enum.Enum):
    active = "Active"
    inactive = "Inactive"

class Volunteer(Base):
    __tablename__ = "volunteers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    phone = Column(String, nullable=False)
    desired_position = Column(String, nullable=False)
    availability = Column(Enum(AvailabilityEnum), nullable=False)
    status = Column(Enum(StatusEnum), nullable=False, default=StatusEnum.active)