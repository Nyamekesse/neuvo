from flask import request, jsonify, make_response, Blueprint
from models.user import User, user_schema
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
    handle_not_processable_error,
)
from sqlalchemy.orm.exc import NoResultFound
from decouple import config

MULTI_AVATAR_API_KEY = config("MULTI_AVATAR_API_KEY")

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
)


def is_username_or_email_taken(username, email):
    user = User.query.filter(
        (User.username == username) | (User.user_email == email)
    ).first()
    return user is not None


def avatar_generator(name):
    avatar = f"https://api.multiavatar.com/{name}.svg?apikey={MULTI_AVATAR_API_KEY}"
    return avatar


@auth_bp.route("/signup", methods=["POST"])
def create_user():
    """create a new user"""
    data = request.get_json()

    if not data:
        return handle_not_processable_error("")
    else:
        try:
            username = data.get("username")
            user_email = data.get("email")
            password = data.get("password")
            confirm_password = data.get("confirmPassword")

            if is_username_or_email_taken(username, user_email):
                return handle_not_processable_error("Username or Email already exist")

            if confirm_password != password:
                return handle_bad_request("Passwords must match")
            new_user = User(
                username=username,
                display_picture=avatar_generator(username),
                user_email=user_email,
                password=generate_password_hash(password).decode("utf-8"),
            )
            new_user.insert()
            new_user = user_schema.dump(new_user)
            return make_response(
                jsonify(
                    {
                        "success": True,
                        "message": "User successfully created",
                        "new_author_id": new_user.get("id"),
                        "new_username": new_user.get("username"),
                    }
                ),
                201,
            )
        except Exception as e:
            print(e)
            return internal_server_error_handler(
                "Something went wrong please try again later"
            )


@auth_bp.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()

    if data is None:
        return handle_not_processable_error("")
    try:
        username_or_email = data.get("usernameOrEmail").strip()
        password = data.get("password").strip()

        check_by_username_or_email = User.query.filter(
            (User.user_email == username_or_email)
            | (User.username == username_or_email)
        ).one()

        if check_by_username_or_email and check_password_hash(
            check_by_username_or_email.password, password
        ):
            profile = user_schema.dump(check_by_username_or_email)
            access_token = create_access_token(identity=profile)
            refresh_token = create_refresh_token(identity=profile)
            return jsonify(
                {
                    "success": True,
                    "message": f"Login successful, welcome {profile.get('username')}",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                }
            )

    except NoResultFound:
        return handle_not_found("User not found")
    except Exception as e:
        print(e)
        return internal_server_error_handler(
            "something went wrong please try again later"
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
    return handle_bad_request("")


@auth_bp.errorhandler(403)
def forbidden_handler(e):
    return handle_forbidden("")


@auth_bp.errorhandler(404)
def not_found_handler(e):
    return handle_not_found("")


@auth_bp.errorhandler(405)
def method_not_allowed_handler(e):
    return handle_method_not_allowed("")


@auth_bp.errorhandler(500)
def internal_server_error_handler(e):
    return handle_internal_server_error("")


@auth_bp.errorhandler(422)
def not_processable_error_handler(e):
    return handle_not_processable_error("")
