__author__ = 'ClarkWong'

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    privilege = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)

    def __init__(self, name, password, privilege=0, description=''):
        self.name = name
        self.password = password
        self.privilege = privilege
        self.description = description





