from flask import Flask, render_template
from . import todo
from . import auth
from .db import db

def create_app():
    app = Flask(__name__)
    
    # Configuración del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///todolist.db'
    )
    
    db.init_app(app)
    
    # Registrar Blueprint
    app.register_blueprint(todo.bp)
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    with app.app_context():
        db.create_all()
    
    return app