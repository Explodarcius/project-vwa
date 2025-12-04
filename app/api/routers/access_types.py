from fastapi import APIRouter
from app.repositories.access_types import get_all_access_types, create_access_type

router = APIRouter(prefix="/access-types", tags=["Access Types"])

@router.get("/")
def list_access_types():
    return get_all_access_types()

@router.post("/")
def add_access_type(name: str):
    new_id = create_access_type(name)
    return {"id": new_id}
