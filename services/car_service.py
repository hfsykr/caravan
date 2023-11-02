from database import db
from models.car_model import Car

def get_car_list():
    query = Car.query.all()
    query = [q.to_dict() for q in query]
    car_list = []
    for q in query:
        car = {}
        car["manufacturer"] = q["manufacturer"]
        car["model"] = q["model"]
        car["type"] = q["type"]
        car["year"] = q["year"]
        car["image"] = q["image"]
        car["slug"] = q["slug"]
        car_list.append(car)
    return car_list