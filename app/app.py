from flask import Flask
from flask import jsonify

from flask_restful import Api
# from flask_jwt_extended import JWTManager
from marshmallow import ValidationError

from db import db, SQLALCHEMY_DATABASE_URI
from ma import ma

from resources.home import Home
from resources.country import Country, CountryList
from resources.city import City, CityList
from resources.region import Region, RegionList
from resources.user import User, UserRegister, UserLogin
from resources.user import TokenRefresh#,UserLogout

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config['JWT_SECRET_KEY'] = "writer"

db.init_app(app)
ma.init_app(app)
# jwt = JWTManager(app)
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400

# @jwt.additional_claims_loader
# def add_claims_to_jwt(identity):
#     if identity == 1:
#         return {'is_admin': True}
#     return {'is_admin': False}

# This method will check if a token is blacklisted, and will be called automatically when blacklist is enabled
# @jwt.token_in_blacklist_loader
# def check_if_token_in_blacklist(decrypted_token):
#     return decrypted_token["jti"] in BLACKLIST

api.add_resource(Home, '/')
api.add_resource(CountryList, '/countries')
api.add_resource(Country, '/country/<string:name>')
api.add_resource(CityList, '/cities')
api.add_resource(City, '/city/<string:name>')
api.add_resource(RegionList, '/regions')
api.add_resource(Region, '/region/<string:name>')

api.add_resource(User, '/User/<int:user_id>')
api.add_resource(UserRegister, "/register")
api.add_resource(UserLogin, "/login")
# api.add_resource(UserLogout, "/logout")
api.add_resource(TokenRefresh, "/refresh")

if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=80, debug=True)
    # app.run(host='0.0.0.0', port=80, debug=True)
    app.run(host='127.0.0.1', port=5000, debug=True)


# https://github.com/teilon/exch_manager/blob/master/schemas/item.py
# https://flask-jwt-extended.readthedocs.io/en/stable/v4_upgrade_guide/