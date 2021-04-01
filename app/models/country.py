from datetime import datetime
from db import db

class CountryModel(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    population = db.Column(db.String(80), nullable=False)
    land_area = db.Column(db.String(80), nullable=True)
    migrants = db.Column(db.String(80), nullable=True)
    medium_age = db.Column(db.String(80), nullable=True)
    urban_pop = db.Column(db.String(80), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, population, land_area, migrants, medium_age, urban_pop):
        self.name = name
        self.population = population
        self.land_area = land_area
        self.migrants = migrants
        self.medium_age = medium_age
        self.urban_pop = urban_pop
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()