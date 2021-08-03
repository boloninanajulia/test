from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restx import Api

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app(env=None):
    from config import get_config
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(get_config(env))
    api = Api(app, title="Flask API", version="0.1.0")

    register_routes(api, app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    return app
