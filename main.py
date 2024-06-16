from fastapi import FastAPI
import implementations.payment_methods as payment_methods
import implementations.movement_type as movement_type
from implementations.database import create_db

app = FastAPI()

app.include_router(payment_methods.route_manager.crud_route, tags=[payment_methods.__name__])
app.include_router(movement_type.route_manager.crud_route, tags=[movement_type.__name__])

app.on_event("startup")(create_db)