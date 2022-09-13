from flask import Flask

# from marvel_inventory.helpers import JSONEncoder
from .site.routes import site
from.authentication.routes import auth
from .api.routes import api
from config import Config

from flask_migrate import Migrate

# Import Models
from covid_inventory.models import db as root_db, login_manager, ma

# Flask-Cors import - Cross Origin Resource Sharing - future proofing api requests
from flask_cors import CORS

# Helpers Import for JSONEncoder
from covid_inventory.helpers import JSONEncoder

app = Flask(__name__)


app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)
app.config.from_object(Config)

root_db.init_app(app)

migrate = Migrate(app, root_db)

login_manager.init_app(app)
login_manager.login_view = 'auth.signin'

ma.init_app(app)

app.json_encoder = JSONEncoder


CORS(app)