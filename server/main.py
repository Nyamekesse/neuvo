from flask import Flask, request
from flask_restx import Api, Resource, fields
from config import DevConfig
from models import User, Post
from flask import jsonify
from exts import db
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    jwt_required,
)

app = Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)
migrate = Migrate(app, db)
Bcrypt(app)
JWTManager(app)
api = Api(app, doc="/docs")
users_model = api.model(
    "Users",
    {
        "id": fields.String(),
        "username": fields.String(),
        "user_email": fields.String(),
        "avatar": fields.String(),
    },
)

posts_model = api.model(
    "Posts",
    {
        "id": fields.String(),
        "title": fields.String(),
        "date_posted": fields.String(),
        "post_content": fields.String(),
        "user_id": fields.String(),
    },
)
create_post_model_data = api.model(
    "Create New Post",
    {
        "title": fields.String(),
        "post_content": fields.String(),
        "user_id": fields.String(),
    },
)
create_user_model_data = api.model(
    "Create New User",
    {
        "username": fields.String(),
        "user_email": fields.String(),
        "password": fields.String(),
        "avatar": fields.String(),
    },
)
login_user_model = api.model(
    "Login User",
    {
        "username": fields.String(),
        "password": fields.String(),
    },
)


@api.route("/hello")
class HelloResource(Resource):
    def get(self):
        return {"msg": "Active!"}


@api.route("/signup")
class SignUp(Resource):
    @api.expect(create_post_model_data)
    def post(self):
        """create a new user"""
        data = request.get_json()
        check_user = User.query.filter_by(username=data.get("username")).first()
        if check_user is not None:
            return jsonify(
                {
                    "success": False,
                    "message": f"User with username {check_user.username} already exist",
                }
            )
        else:
            new_user = User(
                username=data.get("username"),
                user_email=data.get("user_email"),
                password=generate_password_hash(data.get("password")).decode("utf-8"),
                avatar=data.get("avatar"),
            )
            new_user.insert()
            return jsonify({"success": True, "message": "User successfully created"})


# @api.route("/logout")
# def logout():
#     pass


@api.route("/login")
class Login(Resource):
    @api.expect(login_user_model)
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        check_user = User.query.filter_by(username=username).first()

        if check_user and check_password_hash(check_user.password, password):
            access_token = create_access_token(identity=check_user.username)
            refresh_token = create_refresh_token(identity=check_user.username)

            return jsonify(
                {
                    "success": True,
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                }
            )
        else:
            return jsonify(
                {"success": False, "message": "Incorrect username or password"}
            )


@api.route("/users")
class UsersResource(Resource):
    @api.marshal_list_with(users_model)
    def get(self):
        """get all users from database"""
        users = User.query.order_by(User.username).all()
        return users, 200


@api.route("/user/<id>")
class UsersResource(Resource):
    @api.marshal_with(users_model)
    @jwt_required()
    def get(self, id):
        """get specific user from database"""
        user = User.query.get_or_404(id)
        return user, 200

    @api.marshal_with(users_model)
    @jwt_required()
    def put(self, id):
        """update user details in database"""
        data = request.get_json()
        user_to_be_updated = User.query.get_or_404(id)
        user_to_be_updated.update(
            data.get("username"),
            data.get("user_email"),
            data.get("password"),
            data.get("avatar"),
        )
        return user_to_be_updated, 200

    @api.marshal_with(users_model)
    @jwt_required()
    def delete(self, id):
        """delete a user from the database"""
        user_to_be_deleted = User.query.get_or_404(id)
        user_to_be_deleted.delete()
        return user_to_be_deleted, 200


@api.route("/posts")
class PostsResource(Resource):
    @api.marshal_list_with(posts_model)
    def get(self):
        """get all posts from database"""
        posts = Post.query.order_by(Post.title).all()
        return posts, 200

    @api.marshal_with(posts_model)
    @api.expect(create_post_model_data)
    @jwt_required()
    def post(self):
        """create a new post"""
        data = request.get_json()
        new_post = Post(
            title=data.get("title"),
            post_content=data.get("post_content"),
            user_id=data.get("user_id"),
        )
        new_post.insert()
        return new_post, 201


@api.route("/post/<id>")
class PostsResource(Resource):
    @api.marshal_with(posts_model)
    def get(self, id):
        """get a specific post"""
        print(type(id))
        single_post = Post.query.get_or_404(id)
        return single_post

    @api.marshal_with(posts_model)
    @jwt_required()
    def put(self, id):
        """update a specific post"""
        data = request.get_json()
        post_to_update = Post.query.get_or_404(id)
        post_to_update.update(data.get("title"), data.get("post_content"))
        return post_to_update, 200

    @api.marshal_with(posts_model)
    @jwt_required()
    def delete(self, id):
        """delete a specific post"""
        post_to_delete = Post.query.get_or_404(id)
        post_to_delete.delete()

        return post_to_delete, 200


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}


if __name__ == "__main__":
    app.run()
