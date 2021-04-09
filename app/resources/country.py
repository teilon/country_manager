from flask_restful import Resource, request
from flask_jwt_extended import jwt_required
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_optional


from models.country import CountryModel
from schemas.country import CountrySchema

NAME_ALREADY_EXISTS = 'An item with name {} already exists.'
ITEM_NOT_FOUND = 'Item not found.'
ERROR_INSERTING ='An error occurred inserting the item.'
ITEM_DELETED = 'Item {} deleted'

item_schema = CountrySchema()
item_list_schema = CountrySchema(many=True)

class Country(Resource):
        
    @classmethod    
    @jwt_required()
    def get(cls, name: str):
        item = CountryModel.find_by_name(name)
        if item:
            return item_schema.dump(item), 200
        return {'message': ITEM_NOT_FOUND}, 404

    @classmethod
    # @jwt_required(fresh=True)
    def post(cls, name: str):
        if CountryModel.find_by_name(name):
            return {'message': NAME_ALREADY_EXISTS.format(name)}, 400
        
        try:
            data = request.get_json()
        except Exception:
            return {'message': 'Data is empty.'}
        data['name'] = name

        try:
            item = item_schema.load(data)
        except TypeError:
            return {'message': 'Data is not correct.'}
            

        try:
            item.save_to_db()
        except:
            return {'message': ERROR_INSERTING}, 500 
        
        return item_schema.dump(item), 201
        
    @classmethod
    @jwt_required()
    def delete(cls, name: str):
        # claims = get_current_user()
        # if not claims['is_admin']:
        #     return {'message': 'Admin privilege required.'}, 401

        item = CountryModel.find_by_name(name)
        if item:
            item.delete_from_db()
        
        return {'message': ITEM_DELETED.format(name)}

    @classmethod
    @jwt_required
    def put(cls, name: str):
        item_json = request.get_json()
        item = CountryModel.find_by_name(name)

        if item:
            item.population = item_json['population']
            item.land_area = item_json['land_area']
            item.migrants = item_json['migrants']
            item.medium_age = item_json['medium_age']
            item.urban_pop = item_json['urban_pop']
        else:
            item_json['name'] = name
            item = item_schema.load(item_json)
      
        item.save_to_db()
        
        return item_schema.dump(item), 200

class CountryList(Resource):

    @classmethod
    @jwt_required(optional=True)
    def get(cls):
        items = item_list_schema.dump(CountryModel.find_all())
        if items:
            return {'countries': items}, 200
        return {'message': 'Objects list is empty.'}, 200
