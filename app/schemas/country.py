from ma import ma
from marshmallow import EXCLUDE
from models.country import CountryModel

class CountrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CountryModel
        # dump_only = ("id",)
        load_only = ("id",)
        load_instance = True
        unknown = EXCLUDE
        