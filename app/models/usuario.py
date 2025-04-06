from app.config.database import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(15), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "perfil": {
                "rol": self.perfil.rol if self.perfil else None,
                "estado_rostro": self.perfil.estado_registro_facial if self.perfil else None,
                "creado_en": self.perfil.fecha_creacion.isoformat() if self.perfil else None
            } if self.perfil else None
        }
