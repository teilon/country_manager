from flask import Flask, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from db import db, SQLALCHEMY_DATABASE_URI
from ma import ma

from resources.home import Home
from resources.login import Login
from resources.logout import Logout
from resources.item import Item, ItemList
from resources.country import Country, CountryList
from resources.city import City, CityList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400

api.add_resource(Home, '/')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(CountryList, '/countries')
api.add_resource(Country, '/country/<string:name>')
api.add_resource(CityList, '/cities')
api.add_resource(City, '/city/<string:name>')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)


# https://github.com/teilon/exch_manager/blob/master/schemas/item.py