import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    SECRET_KEY = 'my_anac_app'
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/anac_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
