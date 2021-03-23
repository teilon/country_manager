import sqlite3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

SQLITE_DATABASE = 'data.db'


# connection = sqlite3.connect('data.db')
SQLALCHEMY_DATABASE_URI = f'sqlite:///{SQLITE_DATABASE}'
