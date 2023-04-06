from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import shortuuid

app = Flask(__name__)
db = SQLAlchemy()
marshmallow = Marshmallow()
migrate = Migrate()


def gen_short_id():
    return shortuuid.uuid()
