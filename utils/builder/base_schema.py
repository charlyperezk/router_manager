from abc import ABC, abstractmethod
from typing import Dict, Any, Type
from utils.builder.field import Field


class BaseSchema(ABC):

    """
        Abstract class from which all schema classes should inherit.
    """

    __denominator__ = "BuilderBaseSchema"

    @abstractmethod
    async def get_attrs(self) -> Dict[str, Field]:
        raise NotImplementedError("Method not implemented yet.")
    
    async def is_private(self, key: Type[str]):
        if key.startswith("__") and not key.endswith("__"):
            return True
        
    async def is_denominator(self, key: Type[str]):
        if key == "__denominator__":
            return True
    
    async def get_denominator(self) -> str:
        return self.__denominator__

class Diagram(ABC):

    attrs: Dict[str, Any] = {
        "__annotations__": {},
    }
    name: Type[str] = "DiagramBase"

    def impact_field(self, data: Dict[str, Any]):
        self.attrs["__annotations__"][data.name] = data.type
        if "default" in data:
            self.attrs[data.name] = data.default
    
    def get_creational_attrs(self) -> Dict[str, Any]:
        return self.attrs
    
    @abstractmethod
    def get_name(self, denominator: Type[str]) -> str:
        return denominator

class BuilderBaseSchema(BaseSchema, Diagram):

    conditionals: Dict[str, Any] = {}

    @abstractmethod
    async def get_attrs(self) -> Dict[str, Field]:
        raise NotImplementedError("Method not implemented yet.")
    
    @abstractmethod
    async def match(self, field: Field) -> Type[bool]:
        raise NotImplementedError("Method not implemented yet.")
        
    async def get_conditionals(self) -> Dict[str, Any]:
        return self.conditionals
