from abc import ABC, abstractmethod
from typing import TypeVar, Generic


class Field(ABC):

    """
        Abstract class from which all field classes should inherit.
    """

    @abstractmethod
    def serialize(self):
        raise NotImplementedError("Method not implemented yet.")
    
class FieldAttributes(ABC):

    """
        Abstract class from which all field attributes classes should inherit.
    """

    @abstractmethod
    def validate_and_set(self, data: dict):
        raise NotImplementedError("Method not implemented yet.")

F = TypeVar("F", bound=Field)
FA = TypeVar("FA", bound=FieldAttributes)
class CommonField(Generic[F], Generic[FA]):
    
    """
        Generic class to be used as a base for all field classes.
    """

    def __init__(self, **kwargs):
        self.validate_and_set(kwargs)