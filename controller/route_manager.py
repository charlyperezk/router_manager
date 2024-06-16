from pydantic.types import UUID4
import utils
from typing import List
from fastapi import Depends, APIRouter
from fastapi.concurrency import run_in_threadpool


class RouteManager(utils.Dependencies):

    def __init__(self, route_name: str, *args, **kwargs):
        if not isinstance(route_name, str):
            raise utils.exc.InitializationError("Route name must be a string")  
        self.route_name = route_name

        try:
            self.analyze_dependencies(args, kwargs)
        except Exception as e:
            raise utils.exc.InitializationError(f"Initialization failed. Details: {e}")

    @property        
    def crud_route(self):

        router = APIRouter()
        
        @router.post(
                f"/{self.route_name}",
                response_model=self.entity.create,
                description="Create a new object",
                response_description="New object created successfully"
                )

        @utils.decorators.logs(denomination=self.route_name)
        @utils.decorators.time_control        
        async def create(
            new: self.entity.create,
            # user: utils.auth.User = Depends(utils.auth.is_authenticated)
            ):

            @self.error_handler.supervise(
                success_message="Object created successfully",
                error_message="Error creating object",
                return_method_response=True
            )
            async def inner_create():
                try:
                    db_object = self.entity.get_db_model_instance(new)
                    crud_return = await run_in_threadpool(self.crud.create, db_object)
                    return self.entity.get_creational_response(crud_return)
                except Exception as e:
                    raise utils.exc.InvalidInputError(detail=str(e))

            return await inner_create()
        
        @router.get(
                f"/{self.route_name}",
                response_model=List[self.entity.read],
                description="Get all objects",
                response_description="List of objects"
                )
        
        @utils.decorators.logs(denomination=self.route_name)
        @utils.decorators.time_control
        async def read_all():
            @self.error_handler.supervise(
                success_message="Objects read successfully",
                error_message="Error reading objects",
                return_method_response=True
                )
            async def inner_read_all():
                try:
                    results = await run_in_threadpool(self.crud.get_all)
                    return list(map(lambda result: self.entity.get_read_response(result), results))

                except Exception as e:
                    raise utils.exc.NotFoundError(detail=str(e))
                
            return await inner_read_all()
        
        @router.get(
            f"/{self.route_name}/{{id}}",
            response_model=self.entity.read,
            description="Get one object",
            response_description="Object found successfully"
            )
        
        @utils.decorators.logs(denomination=self.route_name)
        @utils.decorators.time_control
        async def read_one(id: UUID4):
            @self.error_handler.supervise(
                success_message="Object read successfully",
                error_message="Error reading object",
                return_method_response=True
                )
            async def inner_read():
                try:
                    db_object = await run_in_threadpool(self.crud.get, id)
                    return self.entity.get_read_response(db_object)
                except Exception as e:
                    raise utils.exc.NotFoundError(detail=str(e))
            
            return await inner_read()

        @router.put(
            f"/{self.route_name}/{{id}}",
            response_model=self.entity.read,
            description="Update an object",
            response_description="Object updated successfully"
            )
        
        @utils.decorators.logs(denomination=self.route_name)
        @utils.decorators.time_control
        async def update(
            id: UUID4,
            update: self.entity.update
            ):

            @self.error_handler.supervise(
                success_message="Object updated successfully",
                error_message="Error updating object",
                return_method_response=True
                )
            async def inner_update():
                try:
                    db_object = await run_in_threadpool(self.crud.update, id, update)
                    return self.entity.get_read_response(db_object)
                
                except Exception as e:
                    raise utils.exc.InvalidInputError(detail=str(e))
                
            return await inner_update()

        @router.delete(
            f"/{self.route_name}/{{id}}",
            description="Delete an object",
            response_description="Object deleted successfully"
            )
        @utils.decorators.logs(denomination=self.route_name)
        @utils.decorators.time_control
        async def delete(id: UUID4):
            @self.error_handler.supervise(
                success_message="Object deleted successfully",
                error_message="Error deleting object",
                return_method_response=True
                )
            async def inner_delete():
                try:
                    db_object = await run_in_threadpool(self.crud.delete, id)
                    return self.entity.get_read_response(db_object)
                except Exception as e:
                    raise utils.exc.NotFoundError(detail=str(e))
                
            return await inner_delete()

        return router            
    