import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-never-know-anything'

    # For local test TODO: based on local or GCP we can configure either of them
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or "postgresql:///demo_user"

    # For postgressql created using user msashish and in CloudSQL
    #SQLALCHEMY_DATABASE_URI = "msashish:///sql-dev-cd1b2ba1"
    #postgres+psycopg2://<db_user>:<db_pass>@<public_ip>/<db_name>?host=/cloudsql/<cloud_sql_instance_name>
    #SQLALCHEMY_DATABASE_URI = \
    #    'postgresql+psycopg2://postgres:ShreeGanesh1@35.223.55.86/postgres?host=/cloudsql/sql-dev-cd1b2ba1'
    SQLALCHEMY_DATABASE_URI = \
        'postgres+pg8000://postgres:ShreeGanesh1@/postgres?unix_sock=/cloudsql/sql-dev-cd1b2ba1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
