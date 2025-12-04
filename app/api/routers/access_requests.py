from fastapi import APIRouter
from app.repositories.access_requests import (
    get_all_requests,
    get_request_by_id,
    create_request,
    update_request_status
)
from app.models.schemas import (
    AccessRequestCreate,
    AccessRequestRead
)

router = APIRouter(prefix="/access-requests", tags=["Access Requests"])

@router.get("/", response_model=list[AccessRequestRead])
def list_requests():
    return get_all_requests()

@router.get("/{request_id}", response_model=AccessRequestRead)
def get_request(request_id: int):
    return get_request_by_id(request_id)

@router.post("/", response_model=AccessRequestRead)
def add_request(data: AccessRequestCreate):
    new_id = create_request(
        data.employee_id,
        data.asset_id,
        data.access_type_id,
        data.reason
    )
    return get_request_by_id(new_id)

@router.post("/{request_id}/approve")
def approve_request(request_id: int, approved_by: int):
    update_request_status(request_id, "approved", approved_by)
    return {"status": "approved"}

@router.post("/{request_id}/reject")
def reject_request(request_id: int, approved_by: int):
    update_request_status(request_id, "rejected", approved_by)
    return {"status": "rejected"}
