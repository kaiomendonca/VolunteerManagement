from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from volunteer_management.core.dependencies import get_db
from volunteer_management.services.volunteer import (
    create_volunteer,
    list_volunteers,
    get_volunteer_by_id,
    update_volunteer
)
from volunteer_management.schemas.volunteer import (
    VolunteerCreate,
    VolunteerResponse,
    VolunteerUpdate
)

router = APIRouter(prefix="/volunteers", tags=["Volunteers"])

@router.post("/", response_model=VolunteerResponse)
def register_volunteer(
    volunteer_in: VolunteerCreate,
    db: Session = Depends(get_db)
):
    return create_volunteer(
        db=db,
        volunteer_in=volunteer_in
    )

@router.get("/")
def volunteers_listed(
    desired_position: str = None,
    availability: str = None,
    status: str = None,
    db: Session = Depends(get_db)
):
    return list_volunteers(
        db=db,
        desired_position=desired_position,
        availability=availability,
        status=status
    )

@router.get("/{volunteer_id}")
def get_volunteer(
    volunteer_id: int,
    db: Session = Depends(get_db)
):
    return get_volunteer_by_id(db=db, volunteer_id=volunteer_id)

@router.put("/{volunteer_id}", response_model=VolunteerResponse)
def update_volunteer_data(
    volunteer_id: int,
    data: VolunteerUpdate,
    db: Session = Depends(get_db)
):
    return update_volunteer(
        db=db,
        volunteer_id=volunteer_id,
        data=data
    )