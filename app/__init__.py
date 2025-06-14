from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .routes import crud, stats
    app.register_blueprint(crud.bp)
    app.register_blueprint(stats.bp)

    return app
