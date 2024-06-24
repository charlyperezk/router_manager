from utils.builder.base_schema import BuilderBaseSchema
from my_project.router_manager.config import RM_BuilderSchema

    
class CreateConditionalSchema(RM_BuilderSchema):

    __denominator__ = "CreateConditionalSchema"
    operation = "Create"
    conditionals = {
        "create": True
    }

class ReadConditionalSchema(BuilderBaseSchema):

    __denominator__ = "ReadConditionalSchema"
    operation = "Read"
    conditionals = {
        "read": True
    }

class UpdateConditionalSchema(BuilderBaseSchema):

    __denominator__ = "UpdateConditionalSchema"
    operation = "Update"
    conditionals = {
        "update": True
    }

class DeleteConditionalSchema(BuilderBaseSchema):
    
    __denominator__ = "DeleteConditionalSchema"
    operation = "Delete"
    conditionals = {
        "delete": True
    }
