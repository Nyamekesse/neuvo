from flask import request, jsonify, make_response, abort, Blueprint
from models.models import User
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from image_utils import generate_default_image

auth_blueprint = Blueprint(
    "auth", __name__, url_prefix="/auth", description="Blueprint for authentication"
)


@auth_blueprint.route("/signup", methods=["POST"])
def create_user():
    """create a new user"""
    data = request.get_json()

    if not data:
        abort(400)
    try:
        username = data.get("username")
        user_email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirmPassword")

        check_user = User.query.filter_by(username=username).first()
        if check_user is not None:
            return jsonify(
                {
                    "success": False,
                    "message": f"User with username {check_user.username.format()} already exist",
                }
            )
        else:
            if confirm_password == password:
                new_user = User(
                    username=username,
                    user_email=user_email,
                    password=generate_password_hash(password).decode("utf-8"),
                )
                new_user.insert()
                return jsonify(
                    {
                        "success": True,
                        "message": "User successfully created",
                        "new_user_id": new_user.id.format(),
                        "new_username": new_user.username.format(),
                    }
                )

            else:
                return make_response(
                    jsonify({"success": False, "message": "Password must match"}),
                    400,
                )
    except:
        abort(400)


@auth_blueprint.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()

    username_or_email = data.get("usernameOrEmail")
    password = data.get("password")

    check_user = User.query.filter_by(username=username_or_email).first()

    if check_user and check_password_hash(check_user.password, password):
        profile = {
            "id": str(check_user.id),
            "username": check_user.username.format(),
            "user_email": check_user.user_email.format(),
            "profile_image": check_user.profile_image.format(),
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
            jsonify({"success": False, "message": "Incorrect username or password"}),
            200,
        )


@auth_blueprint.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh_token():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return make_response(jsonify({"access_token": new_access_token}), 200)


@auth_blueprint.route("/logout")
def logout_user():
    pass
