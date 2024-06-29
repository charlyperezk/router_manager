import utils, db
import controller.route_manager as control


__name__ = "team"

try:
    from examples.database import get_session
    from examples.team.public import entity

    session = get_session()
    crud_client = db.CRUDController(model=entity.db_model)
except Exception as e:
    raise utils.exc.InitializationError(f"Error initializing {__name__}. Details: {e}")

route_manager = control.RouteManager(__name__,
                            entity,
                            crud_client,
                            session
                            )