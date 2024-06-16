from pydantic import BaseModel


class BaseOperationalModel(BaseModel):
    pass

class Create(BaseOperationalModel):
    pass

class Read(BaseOperationalModel):
    pass

class Update(BaseOperationalModel):
    pass



