from flask import Blueprint
from controllers.car_controller import index, predict

car_blueprint = Blueprint("car", __name__)

car_blueprint.route("/", methods=["GET"])(index)
car_blueprint.route("/predict", methods=["post"])(predict)