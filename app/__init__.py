import os
from flask import Flask
from app.config.database import db  # Importar desde config


def create_app():
    app = Flask(__name__)

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DB_PATH = os.path.join(BASE_DIR, 'config', 'database.db')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes.usuarios import usuarios_bp
    app.register_blueprint(usuarios_bp, url_prefix='/api')

    from app.routes.perfiles import perfiles_bp
    app.register_blueprint(perfiles_bp, url_prefix='/api')


    return app
