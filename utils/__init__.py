try:
    from utils import exceptions as exc
    from utils.error_handler import ExceptionHandler as ErrorHandler
    from utils.dependencies import DependenciesSupervisor as Dependencies
    from utils.entity import Entity
    from utils import auth
    from utils import decorators
except ImportError as e:
    print(f"Error importing utils. Details: {e}")