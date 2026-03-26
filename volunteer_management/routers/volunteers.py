from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from volunteer_management.schemas.volunteer import VolunteerCreate, VolunteerResponse
from volunteer_management.core.dependencies import get_db
from volunteer_management.services.volunteer import create_volunteer, list_volunteers

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

    