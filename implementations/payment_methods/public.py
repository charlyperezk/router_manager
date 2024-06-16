import schemas, utils, uuid
from sqlalchemy import Column, String, Boolean, UUID
from pydantic.types import UUID4

from implementations.database import Base


class PaymentMethodCreate(schemas.bom.Create):
    name: str
    description: str

    def dict(self):
        return {
            "name": self.name,
            "description": self.description
        }

class PaymentMethodRead(schemas.bom.Read):
    id: UUID4
    name: str
    description: str

    def dict(self):
        return {
            "id": self.id.__str__(),
            "name": self.name,
            "description": self.description
        }

class PaymentMethodUpdate(schemas.bom.Update):
    name: str
    description: str
    is_active: bool

class PaymentMethod(Base):
    __tablename__ = "payment_methods"
    id = Column(UUID, primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String)
    description = Column(String)
    is_active = Column(Boolean, default=True)

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            # "is_active": self.is_active
        }
    
entity = utils.Entity(
    create=PaymentMethodCreate,
    read=PaymentMethodRead,
    update=PaymentMethodUpdate,
    db_model=PaymentMethod
)
