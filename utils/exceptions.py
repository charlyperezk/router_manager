from fastapi.exceptions import HTTPException

class MissingDependency(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=detail)

class InvalidDependency(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=detail)

class InitializationError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=detail)

class CreationError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

class ReadError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

class UpdateError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

class DeletionError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

class NotFoundError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=404, detail=detail)

class InvalidInputError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

class NotAuthorizedError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=401, detail=detail)