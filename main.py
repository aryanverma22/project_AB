from Books.controller.Runbooks import routes as books
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from Repo.Connection import db
from flask_cors import CORS


def run(config_name):
    app = Flask(__name__)
    # configuration
    app.config['SECRET_KEY'] = 'secretkey'
    secret_key = app.config['SECRET_KEY']
    if config_name:
        app.config.from_object(config_name)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:postgres@localhost:5432/ab"
    return app
app=run('')
CORS(app,response= 'true')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)
migrate = Migrate(app, db)
# posts(app)
books(app, db)


if __name__ == '__main__':
    # db.create_all()
    # app.run(port=300,debug=True)
    app.run(port=3600, debug=True)