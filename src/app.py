import os
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from config import load_config
from db import db
from resources.item import Item
from resources.item import ItemList
from resources.store import Store, StoreList
from resources.user import UserRegister
from security import authenticate
from security import identity

config = load_config()
db_path = config['db_path']

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db_uri_local = app.config['SQLALCHEMY_DATABASE_URI'] = \
#     db_path.as_uri().replace("file://", "sqlite://")
db_uri_local = "sqlite:///data.db"
# print(db_uri_local)  # for debugging
if os.environ.get('DATABASE_URL'):
    db_uri = os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://")
else:
    db_uri = db_uri_local
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.secret_key = 'quetzalcoatl'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
