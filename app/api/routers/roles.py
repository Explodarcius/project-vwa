from fastapi import APIRouter
from app.repositories.roles import get_all_roles, create_role
from app.models.schemas import RoleCreate, RoleRead

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/", response_model=list[RoleRead])
def list_roles():
    return get_all_roles()

@router.post("/", response_model=RoleRead)
def add_role(data: RoleCreate):
    new_id = create_role(data.name)
    return RoleRead(id=new_id, name=data.name)
