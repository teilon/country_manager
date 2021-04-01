from datetime import datetime
from db import db

class CityModel(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    population = db.Column(db.String(80), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    country = db.relationship('CountryModel') # , foreign_keys=country_id    

    def __init__(self, name, population):
        self.name = name
        self.population = population
    
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