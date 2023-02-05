from flask_restx import Resource, Namespace, fields
from flask import request, jsonify, make_response, abort
from models.models import User
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)

auth_ns = Namespace("auth", description="Namespace for authentication")

create_user_model_data = auth_ns.model(
    "Create New User",
    {
        "username": fields.String(),
        "user_email": fields.String(),
        "password": fields.String(),
        "avatar": fields.String(),
    },
)
login_user_model = auth_ns.model(
    "Login User",
    {
        "username": fields.String(),
        "password": fields.String(),
    },
)


@auth_ns.route("/signup")
class SignUp(Resource):
    @auth_ns.expect(create_user_model_data)
    def post(self):
        """create a new user"""
        data = request.get_json()
        if not data:
            abort(400)
        try:
            check_user = User.query.filter_by(username=data.get("username")).first()
            if check_user is not None:
                return jsonify(
                    {
                        "success": False,
                        "message": f"User with username {check_user.username.format()} already exist",
                    }
                )

            else:
                new_user = User(
                    username=data.get("username"),
                    user_email=data.get("email"),
                    password=generate_password_hash(data.get("password")).decode(
                        "utf-8"
                    ),
                    avatar=data.get("avatar"),
                )
                new_user.insert()
                return jsonify(
                    {
                        "success": True,
                        "message": "User successfully created",
                        "new_user": new_user.username.format(),
                    }
                )
        except:
            abort(400)


@auth_ns.route("/login")
class Login(Resource):
    @auth_ns.expect(login_user_model)
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
            return make_response(
                jsonify(
                    {"success": False, "message": "Incorrect username or password"}
                ),
                200,
            )


@auth_ns.route("/refresh")
class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)
        return make_response(jsonify({"access_token": new_access_token}), 200)


@auth_ns.route("/logout")
class Logout(Resource):
    def logout(self):
        pass
