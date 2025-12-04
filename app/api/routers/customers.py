from fastapi import APIRouter
from app.repositories.customers import get_all_customers, get_customer_by_id, create_customer

from app.models.schemas import CustomerCreate, CustomerRead

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.get("/", response_model=list[CustomerRead])
def list_customers():
    return get_all_customers()

@router.get("/{customer_id}", response_model=CustomerRead)
def get_customer(customer_id: int):
    return get_customer_by_id(customer_id)

@router.post("/", response_model=CustomerRead)
def add_customer(data: CustomerCreate):
    new_id = create_customer(data.name)
    return CustomerRead(id=new_id, name=data.name)