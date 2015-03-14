__author__ = 'ClarkWong'

from app import db, app
from flask.ext.restful import reqparse, abort, Api, Resource

api = Api(app)

put_parser = reqparse.RequestParser()
put_parser.add_argument('name', type=str)
put_parser.add_argument('password', type=str)
put_parser.add_argument('privilege', type=int)
put_parser.add_argument('description', type=str)

class UserApi(Resource):
    def get(self, user_id):
        pass

    def delete(self, user_id):
        pass

    def put(self, user_id):
        pass


class UserListApi(Resource):
    def get(self):
        pass

    def post(self):
        pass

api.add_resource(UserListApi, '/users', endpoint='userList')
api.add_resource(UserApi, '/user/<user_id>', endpoint='user')
