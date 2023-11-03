from flask import Flask
from database import db
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from routes.index_routes import index_blueprint
from routes.car_routes import car_blueprint
from routes.error_handlers import page_not_found
from config import DevelopmentConfig, TestingConfig, StagingConfig, ProductionConfig

load_dotenv()

config = {
    "DEVELOPMENT": DevelopmentConfig,
    "TESTING": TestingConfig,
    "STAGING": StagingConfig,
    "PRODUCTION": ProductionConfig
}

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
    app.register_error_handler(404, page_not_found)

    return app