from flask import Flask
from exts import db, marshmallow, migrate

from flask_jwt_extended import JWTManager
from models.user import User
from models.post import Post
from flask_bcrypt import Bcrypt
from blueprints.auth_routes import auth_bp
from blueprints.users_routes import users_bp
from blueprints.posts_routes import post_bp
from blueprints.save_post_route import save_post
from blueprints.like_post_route import like_post
from blueprints.default_routes import default_bp
from flask_cors import CORS
from config import DevConfig


def create_app(config=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    marshmallow.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    Bcrypt(app)
    JWTManager(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(save_post)
    app.register_blueprint(like_post)
    app.register_blueprint(default_bp)

    @app.shell_context_processor
    def make_shell_context():
        return {"db": db, "User": User, "Post": Post}

    return app
