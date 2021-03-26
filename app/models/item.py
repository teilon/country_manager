from datetime import datetime
from db import db

class ItemModel(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    population = db.Column(db.Integer)
    # land_area = db.Column(db.Float(precision=2))
    # density = db.Column(db.Float(precision=2))
    # created_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, population):
        self.name = name
        self.population = population
    
    # def json(self):
    #     return {'name': self.name, 'population': self.population}
    
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