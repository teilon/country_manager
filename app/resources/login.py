from flask_restful import Resource

GREETING = 'it is login'

class Login(Resource):

    def get(self):

        return {'message': GREETING}
