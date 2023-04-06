from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import shortuuid


db = SQLAlchemy()
marshmallow = Marshmallow()
migrate = Migrate()


def gen_short_id():
    return shortuuid.uuid()
