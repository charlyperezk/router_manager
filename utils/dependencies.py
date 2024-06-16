from sqlalchemy.orm import Session
from fastapi import APIRouter
import utils, db


class DependenciesSupervisor:

    """ 
    This class is responsible for managing dependencies between components.
    It is used to analyze dependencies between components and to manage the
    addition and removal of dependencies.
    """

    def __init__(self):
        self.dependencies = {
            "router": None,
            "session": None,
            "entity": None,
            "error_handler": None,
            "crud": None
        }	

    def supervise_instancies(self, *args, **kwargs):

        dependencies = {}	

        for tuple in args:
            for value in tuple:
                if not any([isinstance(value, Session), isinstance(value, utils.Entity), isinstance(value, utils.ErrorHandler), isinstance(value, db.CRUDController)]):
                    raise utils.exc.InvalidDependency("Invalid dependency type")                
                if isinstance(value, APIRouter):
                    dependencies["router"] = value
                if isinstance(value, utils.Entity):
                    dependencies["entity"] = value
                if isinstance(value, utils.ErrorHandler):
                    dependencies["error_handler"] = value
                if isinstance(value, db.CRUDController):
                    dependencies["crud"] = value

        return dependencies
        
    def set_atributes(self, dependencies):
        for key, value in dependencies.items():
            setattr(self, key, value)
        # for key, value in self.dependencies.items():
            # if not hasattr(self, key):
                # raise utils.exc.MissingDependency(f"Missing {key} dependency")
        if not hasattr(self, "entity"):
            raise utils.exc.MissingDependency("Missing entity dependency")
        if not hasattr(self, "error_handler"):
            self.error_handler = utils.ErrorHandler()
        if not hasattr(self, "crud"):
            raise utils.exc.MissingDependency("Missing crud dependency")

    def analyze_dependencies(self, *args, **kwargs):
        try:
            dependencies = self.supervise_instancies(*args, **kwargs)
            self.set_atributes(dependencies)
        
        except Exception as e:
            raise utils.exc.InitializationError(f"Error analyzing dependencies. Message: {e}")

    def add_dependency(self, component, dependency):
        if component in self.dependencies:
            self.dependencies[component].append(dependency)
        else:
            self.dependencies[component] = [dependency]

    def get_dependencies(self, component):
        if component in self.dependencies:
            return self.dependencies[component]
        return []

    def get_all_dependencies(self, component):
        dependencies = self.get_dependencies(component)
        for dependency in dependencies:
            dependencies.extend(self.get_all_dependencies(dependency))
        return dependencies

    def get_all_dependents(self, component):
        dependents = []
        for key, value in self.dependencies.items():
            if component in value:
                dependents.append(key)
        return dependents

    def remove_dependency(self, component, dependency):
        if component in self.dependencies:
            self.dependencies[component].remove(dependency)
        if dependency in self.dependencies:
            self.dependencies[dependency].remove(component)

    def remove_component(self, component):
        if component in self.dependencies:
            del self.dependencies[component]
        for key, value in self.dependencies.items():
            if component in value:
                value.remove(component)

    def get_all_components(self):
        return list(self.dependencies.keys())