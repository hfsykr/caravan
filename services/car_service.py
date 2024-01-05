from database import db
from models.car_model import Car
from sqlalchemy import func

def get_car_list(page, per_page=10):
    query = db.select(Car)
    result = db.paginate(query, page=page, per_page=per_page)
    return result

def search_car_list(search, page, per_page=10):
    query = db.select(Car).filter(func.concat(Car.manufacturer, " ", Car.model, " ", Car.type, " ", Car.year, " ",).ilike(f"%{search}%"))
    result = db.paginate(query, page=page, per_page=per_page)
    return result

def get_car_by_slug(slug):
    query = db.select(Car).filter_by(slug=slug)
    result = db.one_or_404(query)
    return result

def get_slug_by_label(label):
    query = db.select(Car.slug).filter_by(label=label)
    result = db.one_or_404(query)
    return result
