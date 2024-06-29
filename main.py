from fastapi import FastAPI
import examples


app = FastAPI()

app.include_router(
    examples.Team.route_manager.crud_route,
    tags=[examples.Team.__name__]
    )

app.on_event("startup")(examples.db.create_db)