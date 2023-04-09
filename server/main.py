import sys
from flask import Flask
from exts import db, marshmallow, migrate
from logs_config import LOGGING_CONFIG
from flask_jwt_extended import JWTManager
from models.user import User
from models.post import Post
from flask_bcrypt import Bcrypt
from blueprints.auth_routes import auth_bp
from blueprints.users_routes import users_bp
from blueprints.posts_routes import post_bp
from blueprints.save_post_route import save_post_bp
from blueprints.like_post_route import like_post_bp
from blueprints.default_routes import default_bp
from flask_cors import CORS
from config import DevConfig, ProConfig, TestConfig
import os
import logging.config
from errors import handle_internal_server_error


if not os.path.exists("logs"):
    os.mkdir("logs")

# logging.config.dictConfig(LOGGING_CONFIG)


def create_app(config=DevConfig):
    logging.config.dictConfig(LOGGING_CONFIG)
    app = Flask(__name__)
    if app.config.get("ENV") == "production":
        app.config.from_object(ProConfig)
    elif app.config.get("ENV") == "testing":
        app.config.from_object(TestConfig)
    else:
        app.config.from_object(DevConfig)
    CORS(app)
    Bcrypt(app)
    JWTManager(app)
    marshmallow.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(save_post_bp)
    app.register_blueprint(like_post_bp)
    app.register_blueprint(default_bp)

    @app.errorhandler(Exception)
    def handle_exception(e):
        app.logger.debug("Unhandled Exception: %s", str(e))
        return handle_internal_server_error("")

    @app.shell_context_processor
    def make_shell_context():
        return {"db": db, "User": User, "Post": Post}

    return app
