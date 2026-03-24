from sqlalchemy.orm import Session
from volunteer_management.models.volunteer import Volunteer
from volunteer_management.schemas.volunteer import VolunteerCreate

def create_volunteer(db: Session, volunteer_in: VolunteerCreate):
    db_volunteer = Volunteer(**volunteer_in.model_dump())
    db.add(db_volunteer)
    db.commit()
    db.refresh(db_volunteer)
    return db_volunteer    
