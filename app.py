from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models import db, User
from resources import api

app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.additional_claims_loader
def add_claims_to_access_token(user):
    return {'role': user.role}

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=5001)