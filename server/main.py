from flask import Flask
from exts import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models.models import Post, User
from flask_bcrypt import Bcrypt
from blueprints.auth_routes import auth_bp
from blueprints.users_routes import users_bp
from blueprints.posts_routes import post_bp
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
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(post_bp)

    @app.shell_context_processor
    def make_shell_context():
        return {"db": db, "User": User, "Post": Post}

    return app
