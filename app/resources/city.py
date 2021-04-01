from flask_restful import Resource, request
import logging

from models.country import CountryModel
from models.city import CityModel
from schemas.city import CitySchema

NAME_ALREADY_EXISTS = 'An item with name {} already exists.'
ITEM_NOT_FOUND = 'Item not found.'
ERROR_INSERTING ='An error occurred inserting the item.'
ITEM_DELETED = 'Item {} deleted'

item_schema = CitySchema()
item_list_schema = CitySchema(many=True)

class City(Resource):
    def get(self, name):
        item = CityModel.find_by_name(name)
        if item:
            return item_schema.dump(item), 200
        return {'message': ITEM_NOT_FOUND}, 404
    
    def post(self, name):
        if CityModel.find_by_name(name):
            return {'message': NAME_ALREADY_EXISTS.format(name)}, 400
        
        data = request.get_json()
        country = CountryModel.find_by_name(data['country_name'])
        data['name'] = name        
        data['country_id'] = country.id
        # data['country'] = country
        item = item_schema.load(data)

        try:
            item.save_to_db()
        except:
            return {'message': ERROR_INSERTING}, 500 
        
        return item_schema.dump(item), 201
    
    def delete(self, name):
        item = CityModel.find_by_name(name)
        if item:
            item.delete_from_db()
        
        return {'message': ITEM_DELETED.format(name)}
    
    def put(self, name):
        item_json = request.get_json()
        item = CityModel.find_by_name(name)

        if item:
            item.population = item_json['population']
        else:
            item_json['name'] = name
            item = item_schema.load(item_json)       
      
        item.save_to_db()
        
        return item_schema.dump(item), 200

class CityList(Resource):

    def get(self):
        items = item_list_schema.dump(CityModel.find_all())
        if items:
            return {'countries': items}, 200
        return {'message': 'Objects list is empty.'}, 200
