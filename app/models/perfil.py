from datetime import datetime
from app.config.database import db

class Perfil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), unique=True, nullable=False)
    usuario = db.relationship("Usuario", backref=db.backref("perfil", uselist=False))
    
    rol = db.Column(db.String(50), nullable=False)
    estado_registro_facial = db.Column(db.String(50), default='pendiente')
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    departamento = db.Column(db.String(100), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "rol": self.rol,
            "estado_registro_facial": self.estado_registro_facial,
            "fecha_creacion": self.fecha_creacion.isoformat(),
            "departamento": self.departamento
        }
