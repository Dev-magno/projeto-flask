from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ASS601A65F165A50F652677-A1243!!5665DF1A5561FDAS'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.views import homepage
from app.models import Contato