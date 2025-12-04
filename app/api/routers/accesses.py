from fastapi import APIRouter
from app.repositories.accesses import (
    get_all_accesses,
    create_access
)
from app.models.schemas import AccessCreate, AccessRead

router = APIRouter(prefix="/access", tags=["Access"])

@router.get("/", response_model=list[AccessRead])
def list_accesses():
    return get_all_accesses()

@router.post("/", response_model=AccessRead)
def add_access(data: AccessCreate):
    new_id = create_access(
        data.employee_id,
        data.asset_id,
        data.approved_by
    )
    return AccessRead(
        id=new_id,
        employee_id=data.employee_id,
        asset_id=data.asset_id,
        status="active",
        approved_by=data.approved_by
    )
