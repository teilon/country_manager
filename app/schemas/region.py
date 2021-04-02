from ma import ma
from marshmallow import EXCLUDE
from models.region import RegionModel

class RegionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RegionModel
        # dump_only = ("id",)
        load_only = ("id",)
        load_instance = True
        unknown = EXCLUDE
        include_fk = True