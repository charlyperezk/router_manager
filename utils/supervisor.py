from fastapi.responses import JSONResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from functools import wraps
from pydantic import BaseModel


class Supervisor:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

        for arg in args:
            if isinstance(arg, Session):
                self.session = arg

    def supervise(self,
                  success_message: Optional[str] = None,
                  success_status_code: Optional[int] = None,
                  error_message: Optional[str] = None,
                  error_status_code: Optional[int] = None,
                  return_method_response: Optional[bool] = False
                  ):
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                try:
                    result = await func(*args, **kwargs)

                    if return_method_response:
                        if isinstance(result, BaseModel):
                            content = result.dict()
                        if isinstance(result, list):
                            content = list(map(lambda x: x.dict(), result))
                        if isinstance(result, str):
                            content = result
                        
                    else:
                        content = success_message

                    self.session.commit()
                    return JSONResponse(
                        status_code=200 if not success_status_code else success_status_code,
                        content={"message": content}
                    )

                except Exception as e:
                    if self.session:
                        self.session.rollback()
                    if error_message:
                        print(error_message)
                        print(e)
                    raise HTTPException(
                        status_code=400 if not error_status_code else error_status_code,
                        detail=str(e) if not error_message else error_message
                    )
            return wrapper
        return decorator