from .. import db
import datetime as dt

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default= dt.datetime.now(), nullable=False)
    usuarioId = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', back_populates = "compras", uselist=False, single_parent=True)
    productoscompras = db.relationship('ProductoCompra', back_populates = 'compra', cascade = 'all, delete-orphan')
    
    def __repr__(self):
        return f'{Compra : {self.usuarioId}}'
    
    
    def to_json(self):
        compra_json = {
            'id': self.id,
            'fecha': str(self.fecha),
            'usuario': self.usuario.to_json(),
        }
        return compra_json
    
    @staticmethod
    def from_json(compra_json):
        id = compra_json.get('id')
        fecha = compra_json.get('fecha')
        usuarioId = compra_json.get('usuarioId')  
         
        return Compra(
            id = id,
            fecha = fecha,
            usuarioId = usuarioId,  
        )