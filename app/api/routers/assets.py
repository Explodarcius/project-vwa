from fastapi import APIRouter
from app.repositories.assets import (
    get_all_assets,
    get_asset_by_id,
    create_asset
)
from app.models.schemas import AssetCreate, AssetRead

router = APIRouter(prefix="/assets", tags=["Assets"])

@router.get("/", response_model=list[AssetRead])
def list_assets():
    return get_all_assets()

@router.get("/{asset_id}", response_model=AssetRead)
def get_asset(asset_id: int):
    return get_asset_by_id(asset_id)

@router.post("/", response_model=AssetRead)
def add_asset(data: AssetCreate):
    new_id = create_asset(data.customer_id, data.name, data.asset_type_id)
    return AssetRead(
        id=new_id,
        customer_id=data.customer_id,
        name=data.name,
        asset_type_id=data.asset_type_id
    )