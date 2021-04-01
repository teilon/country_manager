from ma import ma
from marshmallow import EXCLUDE
from models.city import CityModel

class CitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CityModel
        # dump_only = ("id",)
        load_only = ("id",)
        load_instance = True
        unknown = EXCLUDE
        include_fk = True