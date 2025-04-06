from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# archivo completo app/config/database.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Este bloque lo usas solo para crear la base de datos
if __name__ == '__main__':
    from app import create_app
    app = create_app()
    with app.app_context():
        db.create_all()
        print("✅ Base de datos creada correctamente.")
