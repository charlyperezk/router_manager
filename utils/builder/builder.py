from typing import Any, Generic, TypeVar, Dict, Type
from abc import ABC, abstractmethod
from utils.builder import Field, Diagram, BuilderBaseSchema, BaseSchema


class ClassGenerator(ABC):
    """
        Abstract class to generate classes.
    """

    @abstractmethod
    async def generate_class(self, diagram: Type[Diagram]):
        raise NotImplementedError("Method not implemented yet.")
    
    @abstractmethod
    async def generate_classes(self, denominator: Type[str], attrs: Dict[str, Any]):
        raise NotImplementedError("Method not implemented yet.")
    
    
class Parser(ABC):
    """
        Abstract class to parse fields and class modeling.
    """

    class_matches: Dict[str, BuilderBaseSchema] = {}

    async def parse(self, fields: Dict[str, Field]) -> Dict[str, BuilderBaseSchema]:
        await self.categorize_fields(fields)
        return {k: v.get_creational_attrs() for k, v in self.class_matches.items()}
    
    async def categorize_fields(self, fields: Dict[str, Field]):
        for k, field_object in fields.items():
            for k1, v in self.class_matches.items():
                v: BuilderBaseSchema
                if await v.match(field_object):
                    await v.impact_field(field_object.serialize())

    async def get_class_matches(self) -> Dict[str, BuilderBaseSchema]:
        for k, v in self.class_matches.items():
            return k, v.get_creational_attrs()


P = TypeVar("P", bound=Parser)
CG = TypeVar("CG", bound=ClassGenerator)

class Builder(Generic[P], Generic[CG]):

    async def build(self, model: BaseSchema):
        attrs: Dict[str, Field] = model.get_attrs()  # Schema
        diagrams: Dict[str, BuilderBaseSchema] = await self.parse(attrs)  # Parser
        classes = await self.generate_classes(
            class_name=model.__denominator__,
            attrs=diagrams
        )

        return classes