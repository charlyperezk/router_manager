import requests
from fastapi import Request
from pydantic import BaseModel
from pydantic.types import UUID4


class User(BaseModel):
    
    id: UUID4
    email: str
    
    def dict(self):
        return {
            "id": self.id.__str__(),
            "email": self.email
            }

def is_authenticated(request: Request):
    req = requests.get(
        url="http://localhost:8000/users/me",
        cookies={
            "growbudget_access_token": request.cookies.get("growbudget_access_token")
            }
        )
    user = req.json()
    return User(id=user.get("id"), email=user.get("email")) if req.status_code == 200 else False
    