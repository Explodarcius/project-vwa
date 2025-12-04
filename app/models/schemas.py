from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# =========================================================
# ROLE
# =========================================================

class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    pass

class RoleRead(RoleBase):
    id: int


# =========================================================
# EMPLOYEE
# =========================================================

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    login: str
    role_id: int

class EmployeeCreate(EmployeeBase):
    password: str  # raw password before hashing

class EmployeeRead(EmployeeBase):
    id: int
    last_login: Optional[datetime] = None


# =========================================================
# CUSTOMER
# =========================================================

class CustomerBase(BaseModel):
    name: str

class CustomerCreate(CustomerBase):
    pass

class CustomerRead(CustomerBase):
    id: int


# =========================================================
# ASSET TYPE
# =========================================================

class AssetTypeBase(BaseModel):
    name: str

class AssetTypeCreate(AssetTypeBase):
    pass

class AssetTypeRead(AssetTypeBase):
    id: int


# =========================================================
# ASSET
# =========================================================

class AssetBase(BaseModel):
    customer_id: int
    name: str
    asset_type_id: int

class AssetCreate(AssetBase):
    pass

class AssetRead(AssetBase):
    id: int


# =========================================================
# ACCESS TYPE
# =========================================================

class AccessTypeBase(BaseModel):
    name: str

class AccessTypeCreate(AccessTypeBase):
    pass

class AccessTypeRead(AccessTypeBase):
    id: int


# =========================================================
# ACCESS REQUEST
# =========================================================

class AccessRequestBase(BaseModel):
    employee_id: int
    asset_id: int
    access_type_id: int
    reason: Optional[str] = None

class AccessRequestCreate(AccessRequestBase):
    pass

class AccessRequestRead(AccessRequestBase):
    id: int
    status: str
    created_at: datetime
    approved_at: Optional[datetime] = None
    approved_by: Optional[int] = None


# =========================================================
# ACCESS (GRANTED)
# =========================================================

class AccessBase(BaseModel):
    employee_id: int
    asset_id: int

class AccessCreate(AccessBase):
    approved_by: int

class AccessRead(AccessBase):
    id: int
    status: str
    approved_by: int


# =========================================================
# AUTHENTICATION
# =========================================================

class LoginRequest(BaseModel):
    login: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    employee_id: Optional[int] = None
