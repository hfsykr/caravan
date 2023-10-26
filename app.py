from flask import Flask

from routes.index_routes import index_blueprint
from routes.car_routes import car_blueprint

app = Flask(__name__)

app.register_blueprint(index_blueprint)
app.register_blueprint(car_blueprint, url_prefix="/car")