import schemas, utils, uuid
from sqlalchemy import Column, String, Boolean, UUID
from pydantic.types import UUID4

from examples.database import Base


class TeamCreate(schemas.bom.Create):
    name: str
    description: str

    def dict(self):
        return {
            "name": self.name,
            "description": self.description
        }

class TeamRead(schemas.bom.Read):
    id: UUID4
    name: str
    description: str

    def dict(self):
        return {
            "id": self.id.__str__(),
            "name": self.name,
            "description": self.description
        }

class TeamUpdate(schemas.bom.Update):
    name: str
    description: str
    is_active: bool

class Team(Base):
    __tablename__ = "team"
    id = Column(UUID, primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String)
    description = Column(String)
    # is_default = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            # "is_active": self.is_active
        }
    
entity = utils.Entity(
    create=TeamCreate,
    read=TeamRead,
    update=TeamUpdate,
    db_model=Team
)
