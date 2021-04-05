from flask import render_template
from flask_restful import Resource

GREETING = 'Hello, man!'

class Home(Resource):

    def get(self):

        context = {
            'greeting': GREETING
        }
        return render_template('index.html', context=context)
        # return {'message': GREETING}
        