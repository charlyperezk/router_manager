from utils.builder.basic_config.config import common_field as CommonField
from utils.builder.basic_config.config import RM_BuilderSchema, builder
import utils, uuid
from implementations.database import Base

from sqlalchemy import Column, String, Boolean, UUID


class MovementType(RM_BuilderSchema):
    __denominator__ = "MovementType"

    id = CommonField(name="id", type=str, modifiable=False, visible=True)
    name = CommonField(name="name", type=str, modifiable=True, visible=True)
    description = CommonField(name="description", type=str, modifiable=True, visible=True)

schema = MovementType()
schemas = builder.build(schema)

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
    schemas=schemas,
    db_model=MovementType
)
