from fastapi import FastAPI
from implementations.database import create_db
import implementations


app = FastAPI()

app.include_router(
    implementations.payment_methods.route_manager.crud_route,
    tags=[implementations.payment_methods.__name__]
    )

app.include_router(
    implementations.movement_type.route_manager.crud_route,
    tags=[implementations.movement_type.__name__]
    )

app.include_router(
    implementations.movement_category.route_manager.crud_route,
    tags=[implementations.movement_category.__name__]
    )

app.on_event("startup")(create_db)