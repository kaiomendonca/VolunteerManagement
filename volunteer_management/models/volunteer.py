# models/volunteer.py
from sqlalchemy import Column, Integer, String, Enum, DateTime
from volunteer_management.database.base import Base
from sqlalchemy.sql import func
import enum

class CargoEnum(str, enum.Enum):
    BACKEND = "backend"
    FRONTEND = "frontend"
    FULLSTACK = "fullstack"

class AvailabilityEnum(str, enum.Enum):
    MORNING = "morning"
    AFTERNOON = "afternoon"
    EVENING = "evening"
    WEEKEND = "weekend"

class StatusEnum(str, enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    


class Volunteer(Base):
    __tablename__ = "volunteers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    phone = Column(String, nullable=False)
    desired_position = Column(Enum(CargoEnum), nullable=False)
    availability = Column(Enum(AvailabilityEnum), nullable=False)
    status = Column(Enum(StatusEnum), nullable=False, default=StatusEnum.ACTIVE)
    created_at = Column(DateTime(timezone=True), server_default=func.now())