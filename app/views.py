__author__ = 'ClarkWong'

from app import db, app
from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with, marshal
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

    @marshal_with(user_fields)
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
            return user, 201
        else:
            abort(404, message='User {} not found'.format(user_id))

    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return { 'message' : 'Delete User {} succeed'.format(user_id)}, 201
        else:
            abort(404, message='User {} not found'.format(user_id))

    @marshal_with(user_fields)
    def put(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
            args = self.parser.parse_args()
            for k,v in args.iteritems():
                if v!= None:
                    setattr(user, k, v)
            db.session.commit()
            return user, 201
        else:
            abort(404, message='User {} not found'.format(user_id))


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
        if userList:
            return [marshal(user, user_fields) for user in userList]
        else:
            abort(404, message='No User at all')

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

api.add_resource(UserListApi, '/api/v1/users', endpoint='userList')
api.add_resource(UserApi, '/api/v1/users/<user_id>', endpoint='user')
