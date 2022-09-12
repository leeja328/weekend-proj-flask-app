# Import from SQLAlchemy
from itertools import count
from flask_sqlalchemy import SQLAlchemy

# flask_migrate imports - sends models to db as tables
from flask_migrate import Migrate

import uuid # sets id for user

# timestamp for user creation
from datetime import datetime

# add flaskL security for hashing passwords
from werkzeug.security import generate_password_hash, check_password_hash

# create a token hex for the user_token
import secrets

# Imports from flash_login
from flask_login import UserMixin, LoginManager

# Imports for Flash-Marshmallow
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(150), nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow )
    drone = db.relationship('Drone', backref = 'owner', lazy = True)

    def __init__(self, email, first_name = '', last_name = '', id = '', password = '', token = '', g_auth_verify = False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify


    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f"User {self.email} has been added to the database!"



class Drone(db.Model):
    id = db.Column(db.String, primary_key = True)
    tested_positive = db.Column(db.Numeric(precision=10, scale=2))
    country = db.Column(db.String(150), nullable = True)
    state = db.Column(db.String(100), nullable = True)
    city = db.Column(db.String(100))
    deaths = db.Column(db.Numeric(precision=10, scale=2))
    series = db.Column(db.String(150))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, tested_positive, country, state, city, deaths, series, user_token, id=''):
        self.id = self.set_id()
        self.tested_positive = tested_positive
        self.country = country
        self.state = state
        self.city = city
        self.deaths = deaths
        self.series = series
        self.user_token = user_token

    def __repr__(self):
        return f"The following location has been added: {self.name}"

    def set_id(self):
        return secrets.token_urlsafe()



class DroneSchema(ma.Schema):
    class Meta:
        fields = ['id', 'tested_positive', 'country', 'state', 'city', 'deaths', 'series']

drone_schema = DroneSchema()
drones_schema = DroneSchema(many = True)

