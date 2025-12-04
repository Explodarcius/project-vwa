from fastapi import FastAPI
from typing import List
import json
from app.api.routers import (
    roles,
    employees,
    customers,
    asset_types,
    assets,
    access_types,
    access_requests,
    accesses
)
from models.schemas import 

def create_app():
    app = FastAPI(
        title="System evidence přístupů",
        version="1.0.0"
    )

    # Register routers
    app.include_router(roles.router)
    app.include_router(employees.router)
    app.include_router(customers.router)
    app.include_router(asset_types.router)
    app.include_router(assets.router)
    app.include_router(access_types.router)
    app.include_router(access_requests.router)
    app.include_router(accesses.router)

    return app

app = create_app()
