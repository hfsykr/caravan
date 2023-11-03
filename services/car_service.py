from database import db
from models.car_model import Car

def get_car_list():
    query = db.select(Car)
    result = db.session.execute(query).scalars()
    result = [r.to_dict() for r in result]
    car_list = []
    for row in result:
        car = {}
        car["manufacturer"] = row["manufacturer"]
        car["model"] = row["model"]
        car["type"] = row["type"]
        car["year"] = row["year"]
        car["image"] = row["image"]
        car["slug"] = row["slug"]
        car_list.append(car)
    return car_list

def get_car_by_slug(slug):
    query = db.select(Car).filter_by(slug=slug)
    result = db.one_or_404(query)
    return result.to_dict()

def get_slug_by_label(label):
    query = db.select(Car.slug).filter_by(label=label)
    result = db.one_or_404(query)
    return result