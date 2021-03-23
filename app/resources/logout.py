from flask_restful import Resource

GREETING = 'it is logout'

class Logout(Resource):

    def get(self):

        return {'message': GREETING}
