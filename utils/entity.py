import schemas
from pydantic import BaseModel
from sqlalchemy.orm.decl_api import DeclarativeMeta


class Entity:
    def __init__(self, create: schemas.bom.Create, read: schemas.bom.Read, update: schemas.bom.Update, db_model: DeclarativeMeta):
        self.create = create
        self.read = read
        self.update = update
        self.db_model = db_model
        if not any([isinstance(self.create, schemas.bom.Create), isinstance(self.read, schemas.bom.Read), isinstance(self.update, schemas.bom.Update), isinstance(self.db_model, DeclarativeMeta)]):
            raise ValueError("Invalid entity schema type")

    def dict(self):
        return {
            "create": self.create,
            "read": self.read,
            "update": self.update,
            "db_model": self.db_model
        }
    
    def get_db_model_instance(self, obj: BaseModel):
        return self.db_model(**obj.dict())
    
    def get_creational_response(self, *args, **kwargs):
        for value in args:
            if isinstance(value, self.db_model):
                return self.create(**value.dict())
            if isinstance(value, list):
                return [self.create(**obj.dict()) for obj in value]
            
    def get_read_response(self, *args, **kwargs):
        for value in args:
            if isinstance(value, self.db_model):
                return self.read(**value.dict())
            if isinstance(value, list):
                return [self.read(**obj.dict()) for obj in value]
