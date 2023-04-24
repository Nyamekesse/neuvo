from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_whooshee import Whooshee

db = SQLAlchemy()
marshmallow = Marshmallow()
migrate = Migrate()
whooshee = Whooshee()
