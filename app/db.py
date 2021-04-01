import sqlite3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

SQLITE_DATABASE = 'data.db'

POSTGRES_HOST = '80.249.147.133' # os.environ['POSTGRES_HOST']
POSTGRES_PORT = '5434' # os.environ['POSTGRES_PORT']
POSTGRES_DATABASE = 'world' # os.environ['POSTGRES_DB']
POSTGRES_USER = 'thror' # os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = 'hammer' # os.environ['POSTGRES_PASSWORD']

# connection = sqlite3.connect('data.db')
SQLALCHEMY_DATABASE_URI = f'sqlite:///{SQLITE_DATABASE}'
# SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.\
#     format(POSTGRES_USER,
#            POSTGRES_PASSWORD,
#            POSTGRES_HOST,
#            POSTGRES_PORT,
#            POSTGRES_DATABASE)