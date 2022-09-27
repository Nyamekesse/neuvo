from flask import Flask
from flask_restx import Api
from exts import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models.models import Post, User
from flask_bcrypt import Bcrypt
from routes.auth_namespace import auth_ns
from routes.posts_namespace import post_ns
from routes.users_namespace import user_ns


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    Migrate(app, db)
    Bcrypt(app)
    JWTManager(app)
    api = Api(app, doc="/docs")
    api.add_namespace(auth_ns)
    api.add_namespace(post_ns)
    api.add_namespace(user_ns)

    @app.shell_context_processor
    def make_shell_context():
        return {"db": db, "User": User, "Post": Post}

    return app
