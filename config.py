import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-never-know-anything'

    # For local test TODO: based on local or GCP we can configure either of them
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or "postgresql:///demo_user"

    # For postgressql created using user msashish and in CloudSQL
    #SQLALCHEMY_DATABASE_URI = "msashish:///sql-dev-cd1b2ba1"
    SQLALCHEMY_DATABASE_URI = \
        'postgresql+psycopg2://msashish:ShreeGanesh1@/postgres?host=/cloudsql/qwiklabs-gcp-00-aa77c6f5d862:us-central1:sql-dev-cd1b2ba1/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
