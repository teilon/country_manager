from flask_restful import Resource, request
# from flask_jwt_extended import jwt_required
import logging

from models.country import CountryModel
from models.region import RegionModel
from schemas.region import RegionSchema

NAME_ALREADY_EXISTS = 'An item with name {} already exists.'
ITEM_NOT_FOUND = 'Item not found.'
ERROR_INSERTING ='An error occurred inserting the item.'
ITEM_DELETED = 'Item {} deleted'

item_schema = RegionSchema()
item_list_schema = RegionSchema(many=True)

class Region(Resource):

    @classmethod
    def get(cls, name):
        item = RegionModel.find_by_name(name)
        if item:
            return item_schema.dump(item), 200
        return {'message': ITEM_NOT_FOUND}, 404
    
    @classmethod
    # @jwt_required()
    def post(cls, name):
        if RegionModel.find_by_name(name):
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
    # @jwt_required()
    def delete(cls, name):
        item = RegionModel.find_by_name(name)
        if item:
            item.delete_from_db()
        
        return {'message': ITEM_DELETED.format(name)}
    
    @classmethod
    # @jwt_required()
    def put(cls, name):
        item_json = request.get_json()
        item = RegionModel.find_by_name(name)
        
        return item_schema.dump(item), 200

class RegionList(Resource):

    @classmethod
    def get(cls):
        items = item_list_schema.dump(RegionModel.find_all())
        if items:
            return {'regions': items}, 200
        return {'message': 'Objects list is empty.'}, 200
