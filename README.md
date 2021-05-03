##  Setup postgresql locally
    Install postgresql from https://postgresapp.com/
    create a DB as below [terminal] 
        psql
        create database demo_user;
        \q
    
##  Create table by using SQLALCHEMY's migrate feature
    
    export SQLALCHEMY_DATABASE_URI="postgresql:///demo_user" 
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade  (to apply changes)
    python initial_data_load.py  (to insert some sample data)
   
    
##  Check table data manually [terminal]
    psql
    \c demo_user
    \dt
    select * from demo_users;
    
##  Test running flask app locally
    python -m flask run (Dont use flask run as it triggers cli.py from outside of venv)
    Check at http://127.0.0.1:5000/ either through Postman for POST and GET 
    
    or run gunicorn
    gunicorn app:app
    Check at  http://127.0.0.1:8000/
    
##  Deploy flask app to GKE using GitHub Actions

    See ---> .github/workflows/gke.yml    
    Reference: https://github.com/google-github-actions/setup-gcloud/blob/master/example-workflows/gke/README.md
    For custom CD use app.yaml and a custom scripto
 
    kubectl expose deployment gke-test --type=LoadBalancer --port 80 --target-port 8080
    kubectl get services  (use external ip to access)
    