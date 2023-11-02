from flask import request, jsonify, render_template
from services.ml_service import inference
from services.car_service import get_car_list

def index():
    return "Car Index!"

def predict():
    result = inference(request)
    
    return jsonify(result)

def list():
    data = get_car_list()
    return render_template("car/list.html", data=data)