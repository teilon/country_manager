import sqlite3
from db import db

class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # , autoincrement=True
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password