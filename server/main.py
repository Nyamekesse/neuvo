from flask import Flask, make_response, jsonify
from flask_restx import Api, Resource
from exts import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models.models import Post, User
from flask_bcrypt import Bcrypt
from routes.auth_namespace import auth_ns
from routes.posts_namespace import post_ns
from routes.users_namespace import user_ns
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
    api = Api(app, doc="/docs")
    api.add_namespace(auth_ns)
    api.add_namespace(post_ns)
    api.add_namespace(user_ns)

    @api.route("/api/hello")
    class HelloResource(Resource):
        def get(self):
            return make_response(jsonify({"msg": "server active"}), 200)

    @app.shell_context_processor
    def make_shell_context():
        return {"db": db, "User": User, "Post": Post}

    return app
