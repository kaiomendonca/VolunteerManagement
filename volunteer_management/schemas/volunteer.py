from pydantic import BaseModel, EmailStr, ConfigDict
from volunteer_management.models.volunteer import (
    AvailabilityEnum,
    StatusEnum,
    PositionEnum,
)
from datetime import datetime
from typing import Optional


class VolunteerCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    desired_position: PositionEnum
    availability: AvailabilityEnum


class VolunteerResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    desired_position: PositionEnum
    availability: AvailabilityEnum
    status: StatusEnum
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class VolunteerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    desired_position: Optional[PositionEnum] = None
    availability: Optional[AvailabilityEnum] = None
