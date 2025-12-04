from fastapi import APIRouter
from app.repositories.employees import (
    get_all_employees,
    get_employee_by_id,
    create_employee,
)
from app.models.schemas import EmployeeCreate, EmployeeRead


router = APIRouter(prefix="/employees", tags=["Employees"])

@router.get("/", response_model=list[EmployeeRead])
def list_employees():
    return get_all_employees()

@router.get("/{employee_id}", response_model=EmployeeRead)
def get_employee(employee_id: int):
    return get_employee_by_id(employee_id)

@router.post("/", response_model=EmployeeRead)
def add_employee(data: EmployeeCreate):
    # NOTE: hashing will be added later in auth step
    new_id = create_employee(
        data.first_name,
        data.last_name,
        data.login,
        data.role_id,
        data.password,  # temporary, will be hashed
    )
    return EmployeeRead(
        id=new_id,
        first_name=data.first_name,
        last_name=data.last_name,
        login=data.login,
        role_id=data.role_id,
        last_login=None
    )