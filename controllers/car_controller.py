from flask import request, jsonify
from services.ml_service import inference

def index():
    return "Car Index!"

def predict():
    result = inference(request)
    
    return jsonify(result)

def list():
    return "Car List!"