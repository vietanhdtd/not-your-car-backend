import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    POSTGRES = {
        'user': os.environ.get("POSTGRES_USER"),
        'pw': os.environ.get("POSTGRES_PWD"),
        'db': os.environ.get("POSTGRES_DB"),
        'host': os.environ.get("POSTGRES_HOST"),
        'port': os.environ.get("POSTGRES_PORT"),
    }   
    DEBUG = True
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY") or "supersekrit"
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FACEBOOK_OAUTH_CLIENT_ID = os.environ.get("FACEBOOK_OAUTH_CLIENT_ID")
    FACEBOOK_OAUTH_CLIENT_SECRET = os.environ.get("FACEBOOK_OAUTH_CLIENT_SECRET")
    OAUTHLIB_INSECURE_TRANSPORT = True