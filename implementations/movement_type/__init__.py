import utils, db
import controller.route_manager as control


__name__ = "movement_type"

try:
    from implementations.database import Base, engine, get_session
    from implementations.movement_type.public import entity

    crud_client = db.CRUDController(session=get_session(), model=entity.db_model)
    supervisor = utils.Supervisor(get_session())
except Exception as e:
    raise utils.exc.InitializationError(f"Error initializing {__name__}. Details: {e}")

def create_db():
    try:
        Base.metadata.create_all(engine, checkfirst=True)
    except Exception as e:
        raise utils.exc.InitializationError(f"Error creating {__name__} database. Details: {e}")


route_manager = control.RouteManager(__name__,
                            entity,
                            crud_client,
                            supervisor,
                            )