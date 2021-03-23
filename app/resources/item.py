from flask_restful import Resource, reqparse

from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('population', type=int, required=True)

    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        return {'message': 'This field cannot be left blank!'}, 404
    
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': f'An item with name {name} already exists.'}, 400
        
        data = Item.parser.parse_args()
        new_item = ItemModel(name, data['population'])

        try:
            new_item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500 
        
        return new_item.json(), 201
    
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        
        return {'message': "Item deleted"}
    
    def put(self, name):
        data = Item.parser.parse_args()
        
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, c)
        else:
            item.population = data['population']     
        
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500 
        
        return item.json(), 201