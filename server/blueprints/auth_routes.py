from flask import request, jsonify, make_response, abort, Blueprint
from models.models import User
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from errors import (
    handle_bad_request,
    handle_forbidden,
    handle_not_found,
    handle_method_not_allowed,
    handle_internal_server_error,
)

auth_bp = Blueprint(
    "auth", __name__, url_prefix="/auth", description="Blueprint for authentication"
)


@auth_bp.route("/signup", methods=["POST"])
def create_user():
    """create a new user"""
    data = request.get_json()

    if not data:
        abort(400, description="No data found")
    try:
        username = data.get("username")
        user_email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirmPassword")

        check_username = User.query.filter_by(username=username).first()
        check_user_email = User.query.filter_by(user_email=user_email).first()
        if check_username is not None:
            return make_response(
                jsonify(
                    {
                        "success": False,
                        "message": f"User with username {check_username.username.format()} already exist",
                    }
                ),
                400,
            )
        elif check_user_email is not None:
            return make_response(
                jsonify(
                    {
                        "success": False,
                        "message": f"The email specified {check_user_email.username.format()} already exist",
                    }
                ),
                400,
            )
        else:
            if confirm_password == password:
                new_user = User(
                    username=username,
                    user_email=user_email,
                    password=generate_password_hash(password).decode("utf-8"),
                )
                new_user.insert()
                return make_response(
                    jsonify(
                        {
                            "success": True,
                            "message": "User successfully created",
                            "new_user_id": new_user.id.format(),
                            "new_username": new_user.username.format(),
                        }
                    ),
                    201,
                )

            else:
                return make_response(
                    jsonify({"success": False, "message": "Password must match"}),
                    400,
                )
    except:
        abort(400)


@auth_bp.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()
    username_or_email = data.get("usernameOrEmail")
    password = data.get("password")

    check_username = User.query.filter_by(username=username_or_email).first()
    check_user_email = User.query.filter_by(user_email=username_or_email).first()
    if check_username:
        if check_password_hash(check_username.password, password):
            profile = {
                "id": str(check_username.id),
                "username": check_username.username.format(),
                "user_email": check_username.user_email.format(),
                "profile_image": check_username.profile_image.format(),
            }
            access_token = create_access_token(identity=profile)
            refresh_token = create_refresh_token(identity=profile)
            return jsonify(
                {
                    "success": True,
                    "message": f"Login successful, welcome {check_username.username.format()}",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                }
            )
    elif check_user_email:
        if check_password_hash(check_user_email.password, password):
            profile = {
                "id": str(check_user_email.id),
                "username": check_username.username.format(),
                "user_email": check_username.user_email.format(),
                "profile_image": check_username.profile_image.format(),
            }
            access_token = create_access_token(identity=profile)
            refresh_token = create_refresh_token(identity=profile)
            return jsonify(
                {
                    "success": True,
                    "message": f"Login successful, welcome {check_user_email.username.format()}",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                }
            )
    else:
        return make_response(
            jsonify(
                {"success": False, "message": "Incorrect username/email or password"}
            ),
            200,
        )


@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh_token():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return make_response(jsonify({"access_token": new_access_token}), 200)


@auth_bp.route("/logout")
def logout_user():
    pass


@auth_bp.errorhandler(400)
def bad_request_handler(e):
    return handle_bad_request(e)


@auth_bp.errorhandler(403)
def forbidden_handler(e):
    return handle_forbidden(e)


@auth_bp.errorhandler(404)
def not_found_handler(e):
    return handle_not_found(e)


@auth_bp.errorhandler(405)
def method_not_allowed_handler(e):
    return handle_method_not_allowed(e)


@auth_bp.errorhandler(500)
def internal_server_error_handler(e):
    return handle_internal_server_error(e)
