from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from routes.index_routes import index_blueprint
from routes.car_routes import car_blueprint
from config import DevelopmentConfig, TestingConfig, StagingConfig, ProductionConfig

load_dotenv()

config = {
    "DEVELOPMENT": DevelopmentConfig,
    "TESTING": TestingConfig,
    "STAGING": StagingConfig,
    "PRODUCTION": ProductionConfig
}

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config[os.getenv("CONFIG")])

    db.init_app(app)
    migrate.init_app(app, db)

    # importing the models to make sure they are known to Flask-Migrate
    from models import car_model

    app.register_blueprint(index_blueprint)
    app.register_blueprint(car_blueprint, url_prefix="/car")

    return app