import utils, schemas


class GenericCRUD:

    def __init__(self, session, model):
        self.session = session
        self.model = model

    def get(self, id: int):
        try:
            obj = self.session.query(self.model).get(id)
            if not obj:
                return None
                # raise utils.exc.NotFoundError(detail=f"{self.model.__name__} not found")
            return obj
        except Exception as e:
            raise utils.exc.ReadError(detail=str(e))
    
    def get_all(self):
        try:
            objects = self.session.query(self.model).all()
            if not objects:
                return []
                # raise utils.exc.NotFoundError(detail=f"No {self.model.__name__} found")
            return objects
        except Exception as e:
            raise utils.exc.ReadError(detail=str(e))
        
    def create(self, obj):
        try:
            self.session.add(obj)
            # self.session.commit()
        except Exception as e:
            raise utils.exc.CreationError(detail=str(e))
        return obj
    
    def update(self, index, updated_object_data: schemas.bom.Update):
        try:
            if isinstance(updated_object_data, schemas.bom.Update):      
                db_register = self.session.query(self.model).filter(self.model.id == index).first()
                for key, value in updated_object_data.dict().items():
                    setattr(db_register, key, value)
                return db_register
            
            else:
                raise utils.exc.InvalidInputError(detail="The updated object data is not a valid object")
        except Exception as e:
            raise utils.exc.UpdateError(detail=str(e))

    def delete(self, id):
        try:
            obj = self.session.query(self.model).get(id)
            self.session.delete(obj)
        except Exception as e:
            raise utils.exc.DeletionError(detail=str(e))
        return obj
