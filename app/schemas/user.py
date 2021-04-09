from ma import ma
from marshmallow import EXCLUDE
from models.user import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id",)

        load_instance = True
        unknown = EXCLUDE