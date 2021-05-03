import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-never-know-anything'

    # For local test TODO: based on local or GCP we can configure either of them
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or "postgresql:///demo_user"

    # For postgressql created using user msashish and in CloudSQL
    SQLALCHEMY_DATABASE_URI = "msashish:///sql-dev-917bf9b7"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
