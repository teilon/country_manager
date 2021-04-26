import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# connection = sqlite3.connect('data.db')
# SQLITE_DATABASE = 'data.db'
# SQLALCHEMY_DATABASE_URI = f'sqlite:///{SQLITE_DATABASE}'

# POSTGRES_USER = "thror"
# POSTGRES_PASSWORD = "hammer"
# POSTGRES_DATABASE = "world"
# POSTGRES_HOST = "80.249.147.133"
# POSTGRES_PORT = "5434"

POSTGRES_HOST = os.environ['POSTGRES_HOST']
POSTGRES_PORT = os.environ['POSTGRES_PORT']
POSTGRES_DATABASE = os.environ['POSTGRES_DATABASE']
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']

SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.\
    format(POSTGRES_USER,
           POSTGRES_PASSWORD,
           POSTGRES_HOST,
           POSTGRES_PORT,
           POSTGRES_DATABASE)

# POSTGRES_USER=thror
# POSTGRES_PASSWORD=hammer
# POSTGRES_DB=world
# host='80.249.147.133'
# port=5432