from .. import db
from main.models import CompraModel

class CompraRepository:

    __modelo = CompraModel

    @property
    def modelo(self):
        return self.__modelo
    
    def find_one(self, id):
        object = db.session.query(self.modelo).get(id)
        return object
    
    def find_all(self):
        objects = db.session.query(self.modelo).all()
        return objects
    
    def create(self, object):
        db.session.add(object)
        db.session.commit()
        return object
    
    def update(self, object):
        self.create(object)
        return object
    
    def delete(self, id):
        object = self.find_one(id)
        db.session.delete(object)
        db.session.commit()
        return object
    
