from flask import Blueprint
from controllers.index_controller import index

index_blueprint = Blueprint("index", __name__)

index_blueprint.route("/", methods=["GET"])(index)