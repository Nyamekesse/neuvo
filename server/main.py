from flask import Flask
from exts import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models.models import Post, User
from flask_bcrypt import Bcrypt
from blueprints.auth_routes import auth_blueprint
from blueprints.users_routes import users_blueprint
from blueprints.posts_routes import post_blueprint
from flask_cors import CORS
from config import DevConfig


def create_app(config=DevConfig):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
    Bcrypt(app)
    JWTManager(app)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(post_blueprint)

    @app.shell_context_processor
    def make_shell_context():
        return {"db": db, "User": User, "Post": Post}

    return app
