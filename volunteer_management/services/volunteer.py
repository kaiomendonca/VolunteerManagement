from sqlalchemy.orm import Session
from volunteer_management.models.volunteer import Volunteer
from volunteer_management.schemas.volunteer import VolunteerCreate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from volunteer_management.models.volunteer import StatusEnum


def create_volunteer(db: Session, volunteer_in: VolunteerCreate):
    db_volunteer = Volunteer(**volunteer_in.model_dump())
    db.add(db_volunteer)

    try:
        db.commit()
        db.refresh(db_volunteer)
        return db_volunteer

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered.")


def list_volunteers(
    db: Session,
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


def get_volunteer_by_id(db: Session, volunteer_id: int):
    volunteer = db.query(Volunteer).filter(volunteer_id == Volunteer.id).first()

    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")

    return volunteer


def update_volunteer(db: Session, volunteer_id: int, data):
    volunteer = db.query(Volunteer).filter(volunteer_id == Volunteer.id).first()

    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(volunteer, key, value)

    try:
        db.commit()
        db.refresh(volunteer)
        return volunteer

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409, detail="Email already exists. Update data correctly"
        )


def inactive_volunteer(db: Session, volunteer_id: int):
    volunteer = db.query(Volunteer).filter(volunteer_id == Volunteer.id).first()

    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")

    if volunteer.status == StatusEnum.INACTIVE:
        raise HTTPException(status_code=400, detail="Volunteer already inactive")

    volunteer.status = StatusEnum.INACTIVE
    db.commit()
    db.refresh(volunteer)

    return {"message": "Volunteer deactivated sucessfully"}
