from flask import Flask,request
from flask_restful import Resource, Api
from decathon import ComputeDecathon


app = Flask(__name__)
api = Api(app)


class Welcome(Resource):    
    def get(self):        
        return {'hello': 'Welcome to Decathon Calculator'}


class Decathon(Resource):
    def post(self):
        data = request.get_json(force=True)
        if "url" in data :
            try:
                cls = ComputeDecathon(data['url']).get_score_and_rank()
                return {'status_message': "Okay",
                        'data': cls.to_dict(orient='records')}, 200
            except Exception as ex:
                return {'status_message': ex.args,
                    'data': None}, 400
        else:
            return {'status_message':"Bad Request",
                    'data': None}, 406
    
api.add_resource(Welcome, '/')
api.add_resource(Decathon, '/api/score/')

if __name__ == '__main__':
    app.run(debug=True)