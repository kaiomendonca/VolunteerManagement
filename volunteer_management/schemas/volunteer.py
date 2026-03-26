from pydantic import BaseModel, EmailStr
from volunteer_management.models.volunteer import AvailabilityEnum, StatusEnum, CargoEnum
from datetime import datetime
from typing import Optional

class VolunteerCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    desired_position: CargoEnum
    availability: AvailabilityEnum
    
class VolunteerResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    desired_position: CargoEnum
    availability: AvailabilityEnum
    status: StatusEnum
    created_at: datetime

    class Config:
        from_attributes = True
        
class VolunteerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    desired_position : Optional[CargoEnum] = None
    availability: Optional[AvailabilityEnum] = None
    