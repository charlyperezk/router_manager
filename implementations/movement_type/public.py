import schemas, utils, uuid
from sqlalchemy import Column, String, Boolean, UUID
from pydantic.types import UUID4

from implementations.database import Base


class MovementTypeCreate(schemas.bom.Create):
    name: str
    description: str

    def dict(self):
        return {
            "name": self.name,
            "description": self.description
        }

class MovementTypeRead(schemas.bom.Read):
    id: UUID4
    name: str
    description: str

    def dict(self):
        return {
            "id": self.id.__str__(),
            "name": self.name,
            "description": self.description
        }

class MovementTypeUpdate(schemas.bom.Update):
    name: str
    description: str
    is_active: bool

class MovementType(Base):
    __tablename__ = "movement_type"
    id = Column(UUID, primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String)
    description = Column(String)
    is_default = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            # "is_active": self.is_active
        }
    
entity = utils.Entity(
    create=MovementTypeCreate,
    read=MovementTypeRead,
    update=MovementTypeUpdate,
    db_model=MovementType
)
