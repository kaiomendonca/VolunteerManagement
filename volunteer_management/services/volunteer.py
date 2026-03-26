from sqlalchemy.orm import Session
from volunteer_management.models.volunteer import Volunteer
from volunteer_management.schemas.volunteer import VolunteerCreate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def create_volunteer(db: Session, volunteer_in: VolunteerCreate):
    db_volunteer = Volunteer(**volunteer_in.model_dump())
    db.add(db_volunteer)
    
    try:
        db.commit()
        db.refresh(db_volunteer)
        return db_volunteer
    
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code = 400,
            detail="Email already registered."
        )     


def list_volunteers(db: Session,
    desired_position: str = None,
    availability: str = None,
    status: str = None,
):

    query = db.query(Volunteer)

    if status:
        query = query.filter(Volunteer.status == status)

    if desired_position:
        query = query.filter(Volunteer.desired_position == desired_position)

    if availability:
        query = query.filter(Volunteer.availability == availability)

    return query.all()
