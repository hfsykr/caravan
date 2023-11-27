from database import db
from uuid import uuid4
from datetime import datetime
from slugify import slugify

def default_slug(context):
    params = context.get_current_parameters()
    slug = (params["manufacturer"] + "-" + params["model"] + "-" + params["type"] + "-" + str(params["year"])).lower()
    clean_slug = slugify(slug)
    return clean_slug

class Car(db.Model):
    id               = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid4, nullable=False, unique=True)
    label            = db.Column(db.Integer, nullable=False, unique=True)
    manufacturer     = db.Column(db.String, nullable=False)
    model            = db.Column(db.String, nullable=False)
    type             = db.Column(db.String, nullable=False)
    year             = db.Column(db.Integer, nullable=False)
    engine           = db.Column(db.String)
    horsepower       = db.Column(db.String)
    torque           = db.Column(db.String)
    transmission     = db.Column(db.String)
    drivetrain       = db.Column(db.String)
    doors            = db.Column(db.Integer)
    seating_capacity = db.Column(db.Integer)
    fuel_type        = db.Column(db.String)
    fuel_capacity    = db.Column(db.String)
    fuel_consumption = db.Column(db.String)
    weight           = db.Column(db.String)
    length           = db.Column(db.String)
    width            = db.Column(db.String)
    height           = db.Column(db.String)
    image            = db.Column(db.String)
    slug             = db.Column(db.String, default=default_slug, nullable=False, unique=True)
    created          = db.Column(db.DateTime(timezone=True), default=datetime.now)   
    updated          = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return "<%r>" % self.slug