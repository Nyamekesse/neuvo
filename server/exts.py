import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_whooshee import Whooshee
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in

db = SQLAlchemy()
marshmallow = Marshmallow()
migrate = Migrate()
whooshee = Whooshee()

# Define the Whoosh schema
schema = Schema(id=ID(stored=True), title=TEXT(stored=True), post_content=TEXT)

# Create the Whoosh index
indexdir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "whoosh_index")
if not os.path.exists(indexdir):
    os.mkdir(indexdir)

ix = create_in(indexdir, schema)
