from pydantic import BaseModel
from typing import Dict, Type

from utils.builder import Field, FieldAttributes, BuilderBaseSchema, ClassGenerator, Parser, Builder, CommonField, Diagram

from my_project.router_manager.schema import CreateConditionalSchema, ReadConditionalSchema, UpdateConditionalSchema, DeleteConditionalSchema


#                                General configuration of the routermanager

# Builder module: 
#   Common-field:

# Field
class RM_Field(Field):

    def serialize(self):
        attrs = vars(self)
        data = {}
        if "type" in attrs:
            data["type"] = self.type.__name__
        if "default" in attrs:
            data["default"] = self.default
        return data

# FieldAttributes    
class RM_FieldAttributess(FieldAttributes):

    def validate_and_set(self, data: dict): # Declarated 
        for key, value in data:

            if key == "type":
                if isinstance(value, type):
                    self.type = value
                else:
                    raise ValueError("Type must be a valid type class.")
                        
            elif key == "modifiable":
                if isinstance(value, bool):
                    self.modifiable = value
                else:
                    raise ValueError("Modifiable must be a boolean.")

            elif key == "visible":
                if isinstance(value, bool):
                    self.visible = value
                else:
                    raise ValueError("Visible must be a boolean.")

            elif key == "default":
                if isinstance(value, self.type):
                    self.default = value

            elif key == "required":
                if isinstance(value, bool):
                    self.required = value
                else:
                    raise ValueError("Required must be a boolean.")

            elif key == "unique":
                if isinstance(value, bool):
                    self.unique = value
                else:
                    raise ValueError("Unique must be a boolean.")

            elif key == "read_only":
                if isinstance(value, bool):
                    self.read_only = value
                else:
                    raise ValueError("Read only must be a boolean.")
                
            elif key == "write_only":
                if isinstance(value, bool):
                    self.write_only = value
                else:
                    raise ValueError("Write only must be a boolean.")

common_field = CommonField[RM_Field, RM_FieldAttributess]


class RM_BuilderSchema(BuilderBaseSchema):

    def get_name(self, denominator: type[str]) -> str:
        return f"{denominator}{self.operation}"

    def get_attrs(self) -> Dict[str, Field]:
        attrs = vars(self)
        return {k: v for k, v in attrs.items() if not self.is_private(k) and not self.is_denominator(k) and self.is_a_field_object(v)}

    def is_a_field_object(self, value: Type[Field]):
        return isinstance(value, Field)
    
    def match(self, field: Type[Field]):
        for key, value in self.get_conditionals().items():
            if len(set(field.get_attrs().keys()).intersection(value.keys())) == len(value.keys()):
                return True

class RM_Parser(Parser):
    
    class_matches = {
        "create": CreateConditionalSchema(),
        "read": ReadConditionalSchema(),
        "update": UpdateConditionalSchema(),
        "delete": DeleteConditionalSchema()
    }

class RM_ClassGenerator(ClassGenerator):

    """
    This class contains the main methods for generating classes based on the provided attributes.
    """

    def generate_class(self, denominator: Type[str], diagram: Type[Diagram]) -> BaseModel:
        new_class = type(diagram.get_name(denominator), (BaseModel), diagram.get_creational_attrs())
        return new_class
    
    def generate_classes(self, denominator: Type[str], diagrams: Dict[Diagram]) -> Dict[str, BaseModel]:
        classes = {}
        for key, value in diagrams.items():
            classes[key.name] = self.generate_class(denominator, value)
        return classes


parser_builder = RM_Parser()
class_generator = RM_ClassGenerator()
builder = Builder[parser_builder, class_generator]




            
