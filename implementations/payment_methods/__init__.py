import utils, db
import controller.route_manager as control

try:
    from implementations.payment_methods.database import Base, engine, get_session
    from implementations.payment_methods.main import payment_method_entity as entity

    crud_client = db.CRUDController(session=get_session(), model=entity.db_model)
    payment_meth_supervisor = utils.Supervisor(get_session())
except Exception as e:
    raise utils.exc.InitializationError(f"Error initializing payment methods. Details: {e}")

def create_payment_meth_db():
    try:
        Base.metadata.create_all(engine, checkfirst=True)
    except Exception as e:
        raise utils.exc.InitializationError(f"Error creating payment methods database. Details: {e}")


route_name = "payment_methods"
route_manager = control.RouteManager(route_name,
                            entity,
                            crud_client,
                            payment_meth_supervisor,
                            )