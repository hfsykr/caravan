from flask import request, abort, redirect, url_for, render_template
from services.ml_service import inference
from services.car_service import get_car_list, get_car_by_slug, get_slug_by_label

def predict():
    if request.method != "POST":
        abort(400)
    result = inference(request)
    slug = get_slug_by_label(result["label"])
    return redirect(url_for('car.detail', slug=slug))

def list():
    data = get_car_list()
    return render_template("car/list.html", data=data)

def detail(slug):
    data = get_car_by_slug(slug)
    return render_template("car/detail.html", data=data)