from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from volunteer_management.schemas.volunteer import VolunteerCreate, VolunteerResponse
from volunteer_management.core.dependencies import get_db
from volunteer_management.services.volunteer import create_volunteer

router = APIRouter(prefix="/volunteers", tags=["Volunteers"])

@router.post("/", response_model=VolunteerResponse)
def register_volunteer(volunteer_in: VolunteerCreate, db: Session = Depends(get_db)):
    return create_volunteer(db=db, volunteer_in=volunteer_in)
    