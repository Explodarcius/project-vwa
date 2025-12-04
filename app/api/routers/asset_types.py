from fastapi import APIRouter
from app.repositories.access_types import get_all_access_types, create_access_type
from app.models.schemas import AccessTypeCreate, AccessTypeRead

router = APIRouter(prefix="/access-types", tags=["Access Types"])

@router.get("/", response_model=list[AccessTypeRead])
def list_access_types():
    return get_all_access_types()

@router.post("/", response_model=AccessTypeRead)
def add_access_type(data: AccessTypeCreate):
    new_id = create_access_type(data.name)
    return AccessTypeRead(id=new_id, name=data.name)
