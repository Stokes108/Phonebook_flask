from  flask import Flask, render_template
from config import Config
from .site.routes import site
from .api.routes import api
from .authentication.routes import auth

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma
from flask_cors import CORS
from helpers import JSONEncoder





# create instance of flask in the app varible
app = Flask(__name__)
CORS(app)

# Put all the html sites connected to app Flask object 
# With the site blueprint object - which has HTML stuff and routes
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

app.json_encoder = JSONEncoder
app.config.from_object(Config)


# initiates the database app (db is a SQLAlchemy object)
root_db.init_app(app)
login_manager.init_app(app)

#links the marshmallow object to the app- 
# ma in charge of connecting and adding stuff to db 
ma.init_app(app)
migrate = Migrate(app, root_db)
   


