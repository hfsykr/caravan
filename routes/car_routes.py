from flask import Blueprint
from controllers.car_controller import detail, predict, list

car_blueprint = Blueprint("car", __name__)

car_blueprint.route("/predict", methods=["POST"])(predict)
car_blueprint.route("/list", methods=["GET"])(list)
car_blueprint.route("/<slug>", methods=["GET"])(detail)