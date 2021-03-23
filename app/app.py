from flask import Flask
from flask_restful import Api

from db import db, SQLALCHEMY_DATABASE_URI

from resources.home import Home
from resources.login import Login
from resources.logout import Logout
from resources.item import Item, ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Home, '/')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)