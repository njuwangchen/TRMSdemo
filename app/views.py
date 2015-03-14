__author__ = 'ClarkWong'

from app import db, app
from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with, marshal
from flask import jsonify
from models import User

api = Api(app)

user_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'password' : fields.String,
    'privilege' : fields.Integer,
    'description' : fields.String
}

class UserApi(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str)
        self.parser.add_argument('password', type=str)
        self.parser.add_argument('privilege', type=int)
        self.parser.add_argument('description', type=str)
        super(UserApi, self).__init__()

    def get(self, user_id):
        pass

    def delete(self, user_id):
        pass

    def put(self, user_id):
        pass


class UserListApi(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True)
        self.parser.add_argument('password', type=str, required=True)
        self.parser.add_argument('privilege', type=int, required=True)
        self.parser.add_argument('description', type=str)
        super(UserListApi, self).__init__()

    def get(self):
        userList = User.query.all()
        return [marshal(user, user_fields) for user in userList]

    @marshal_with(user_fields)
    def post(self):
        args = self.parser.parse_args()
        name = args['name']
        password = args['password']
        privilege = args['privilege']
        description = args['description']
        user = User(name, password, privilege, description)
        db.session.add(user)
        db.session.commit()
        return user, 201

api.add_resource(UserListApi, '/users', endpoint='userList')
api.add_resource(UserApi, '/user/<user_id>', endpoint='user')
