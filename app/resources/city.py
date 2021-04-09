from flask_restful import Resource, request
from flask_jwt_extended import jwt_required
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

    @classmethod
    def get(cls, name):
        item = CityModel.find_by_name(name)
        if item:
            return item_schema.dump(item), 200
        return {'message': ITEM_NOT_FOUND}, 404
    
    @classmethod
    # @jwt_required
    def post(cls, name):
        if CityModel.find_by_name(name):
            return {'message': NAME_ALREADY_EXISTS.format(name)}, 400
        
        item_json = request.get_json()
        country = CountryModel.find_by_name(item_json['country_name'])
        
        item_json['name'] = name        
        item_json['country_id'] = country.id
        item = item_schema.load(item_json)

        try:
            item.save_to_db()
        except:
            return {'message': ERROR_INSERTING}, 500 
        
        return item_schema.dump(item), 201
    
    @classmethod
    @jwt_required()
    def delete(cls, name):
        item = CityModel.find_by_name(name)
        if item:
            item.delete_from_db()
        
        return {'message': ITEM_DELETED.format(name)}
    
    @classmethod
    @jwt_required()
    def put(cls, name):
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

    @classmethod
    def get(cls):
        items = item_list_schema.dump(CityModel.find_all())
        if items:
            return {'cities': items}, 200
        return {'message': 'Objects list is empty.'}, 200
