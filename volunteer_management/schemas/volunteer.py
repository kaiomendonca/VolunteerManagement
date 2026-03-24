from pydantic import BaseModel, EmailStr
from models.volunteer import AvailabilityEnum, StatusEnum, CargoEnum
from datetime import datetime

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