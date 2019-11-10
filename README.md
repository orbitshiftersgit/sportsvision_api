###Create virtual environment
python -m venv venv
### to activate venv
source venv/bin/activate
### to install all requirements
pip install -r requirements.txt
### data base creation
create data base with name sports
postgresql://postgres:abcdef@localhost:5432/sports
### to create migrations
1.  db init
2.  db migrate -m "users table"
3.  db upgrade
### resource to learn flask rest api
1. [restful-api-with-flask](https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way)
2. [crud-web-app](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one)