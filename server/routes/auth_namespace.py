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
        "email": fields.String(),
        "password": fields.String(),
        "confirmPassword": fields.String(),
        # "avatar": fields.String(),
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
        print(data)
        if not data:
            abort(400)
        try:
            username = data.get("username")
            user_email = data.get("email")
            password = data.get("password")
            confirm_password = data.get("confirmPassword")
            check_user = User.query.filter_by(username=username).first()
            if check_user is not None:
                print("hi")
                return jsonify(
                    {
                        "success": False,
                        "message": f"User with username {check_user.username.format()} already exist",
                    }
                )
            else:
                print("fccccccccccccccc")
                new_user = User(
                    username=username,
                    user_email=user_email,
                    password=generate_password_hash(password).decode("utf-8"),
                    profile_image="",
                )
                new_user.insert()
                print("ppppppppppppppppp")
                return jsonify(
                    {
                        "success": True,
                        "message": "User successfully created",
                        "new_user": new_user.username.format(),
                    }
                )

            # else:
            #     return make_response(
            #         jsonify({"success": False, "message": "Password must match"}),
            #         400,
            #     )
        except:
            abort(400)


@auth_ns.route("/login")
class Login(Resource):
    @auth_ns.expect(login_user_model)
    def post(self):
        data = request.get_json()

        username_or_email = data.get("usernameOrEmail")
        password = data.get("password")

        check_user = User.query.filter_by(username=username_or_email).first()

        if check_user and check_password_hash(check_user.password, password):
            profile = {
                "id": str(check_user.id),
                "username": check_user.username.format(),
                "user_email": check_user.user_email.format(),
                "avatar": check_user.avatar.format(),
            }
            access_token = create_access_token(identity=profile)
            refresh_token = create_refresh_token(identity=profile)

            return jsonify(
                {
                    "success": True,
                    "message": f"Login successful, welcome {check_user.username.format()}",
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
