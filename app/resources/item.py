from flask_restful import Resource, request

from models.item import ItemModel
from schemas.item import ItemSchema

NAME_ALREADY_EXISTS = 'An item with name {} already exists.'
ITEM_NOT_FOUND = 'Item not found.'
ERROR_INSERTING ='An error occurred inserting the item.'
ITEM_DELETED = 'Item {} deleted'

item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)

class Item(Resource):
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item_schema.dump(item), 200
        return {'message': ITEM_NOT_FOUND}, 404
    
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': NAME_ALREADY_EXISTS.format(name)}, 400
        
        data = request.get_json()
        data['name'] = name
        item = item_schema.load(data)

        try:
            item.save_to_db()
        except:
            return {'message': ERROR_INSERTING}, 500 
        
        return item_schemam.dump(item), 201
    
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        
        return {'message': ITEM_DELETED.frmat(name)}
    
    def put(self, name):
        item_json = request.get_json()
        item = ItemModel.find_by_name(name)

        if item:
            item.population = item_json['population']
        else:
            item_json['name'] = name
            item = item_schema.load(item_json)       
      
        item.save_to_db()
        
        return item_schema.dump(item), 200

class ItemList(Resource):

    def get(self):
        items = item_list_schema.dump(ItemModel.find_all())
        if items:
            return {'items': items}, 200
        return {'message': 'Objects list is empty/'}, 200
