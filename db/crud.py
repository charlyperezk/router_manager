import utils, schemas


class GenericCRUD:

    def __init__(self, session, model):
        self.session = session
        self.model = model

    def get(self, id: int):
        obj = self.session.query(self.model).get(id)
        if obj is None:
            raise utils.exc.NotFoundError(detail=f"{self.model.__object_name__} not found")
        return obj
    
    def get_all(self):
        try:
            objects = self.session.query(self.model).all()
            if not objects:
                raise utils.exc.NotFoundError(detail=f"No {self.model.__object_name__} found")
            return objects
        except Exception as e:
            raise utils.exc.NotFoundError(detail=str(e))
        
    def create(self, obj):
        try:
            self.session.add(obj)
            # self.session.commit()
        except Exception as e:
            # self.session.rollback()
            raise utils.exc.CreationError(detail=str(e))
        return obj
    
    def update(self, index, updated_object_data: schemas.bom.Update):
        if isinstance(updated_object_data, schemas.bom.Update):      
            db_register = self.session.query(self.model).filter(self.model.id == index).first()
            for key, value in updated_object_data.dict().items():
                setattr(db_register, key, value)
            self.session.commit()
            return db_register
        
        else:
            raise utils.exc.InvalidInputError(detail="The updated object data is not a valid object")
        
    def delete(self, id):
        try:
            obj = self.session.query(self.model).get(id)
            self.session.delete(obj)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise utils.exc.DeletionError(detail=str(e))
        return obj
