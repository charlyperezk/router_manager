try:
    from utils import exceptions as exc
    from utils.supervisor import Supervisor
    from utils.dependencies import DependenciesSupervisor as Dependencies
    from utils.entity import Entity
    from utils import auth
    from utils import decorators as dec
except ImportError as e:
    print(f"Error importing utils. Details: {e}")