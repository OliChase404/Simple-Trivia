from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from sqlalchemy import MetaData

app = Flask(__name__)
app.secret_key = "Well hey there, hello! Welcome to my app and well done for finding the secret key!"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db = SQLAlchemy()

bcrypt = Bcrypt(app)

migrate = Migrate(app, db, render_as_batch=True)

metadata = MetaData()

db.init_app(app)