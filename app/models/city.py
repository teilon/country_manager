from datetime import datetime
from db import db

class CityModel(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    population = db.Column(db.String(80), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    country = db.relationship('CountryModel', foreign_keys=country_id, cascade="all, delete")

    # country = db.relationship("CountryModel",
    #                 backref=backref("countries", cascade="all, delete-orphan")
    #             )
    # country = db.relationship("CountryModel", cascade="all, delete", backref="city", foreign_keys=country_id)
    # reviews = db.relationship('Review', backref='user', cascade='all, delete, delete-orphan')

    # order = relationship("Order",
    #                 backref=backref("items", cascade="all, delete-orphan")
    #             )
    # __table_args__ = (
    #     db.ForeignKeyConstraint(
    #         ["fk_useraccess", "fk_useraccess_level"],
    #         ["countries.id", "cities.country_id"],
    #         ondelete="CASCADE"
    #     )


    def __init__(self, name, population, country_id):
        self.name = name
        self.population = population
        self.country_id = country_id
    
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