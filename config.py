import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, 'env'))

class Config():
    '''
        Set the config variables for the flask app
        using Enviroment variables where available .
        OTherwise, create the config variables if not done already.
    '''

    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'This is crazy stupid'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
