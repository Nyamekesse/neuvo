from flask import request, jsonify, make_response, abort, Blueprint
from models.user import User
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

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
)


def is_username_or_email_taken(username, email):
    # Query the database to check if a user with the given username or email already exists
    user = User.query.filter(
        (User.username == username) | (User.user_email == email)
    ).first()

    # Return True if a user with the given username or email exists, False otherwise
    return user is not None


@auth_bp.route("/signup", methods=["POST"])
def create_user():
    """create a new user"""
    data = request.get_json()

    if not data:
        abort(400, description="No data found")
    else:
        try:
            username = data.get("username").strip()
            user_email = data.get("email").strip()
            password = data.get("password").strip()
            confirm_password = data.get("confirmPassword").strip()

            default = "https://www.dovercourt.org/wp-content/uploads/2019/11/610-6104451_image-placeholder-png-user-profile-placeholder-image-png.jpg"
            if is_username_or_email_taken(username, user_email):
                return make_response(
                    jsonify(
                        {
                            "success": False,
                            "message": "Username or email already taken",
                        }
                    ),
                    400,
                )

                return make_response(
                    jsonify(
                        {
                            "success": False,
                            "message": f"The email specified {check_user_by_email.username.format()} already exist",
                        }
                    ),
                    400,
                )

            if confirm_password == password:
                new_user = User(
                    username=username,
                    display_picture=default,
                    user_email=user_email,
                    password=generate_password_hash(password).decode("utf-8"),
                )
                new_user.insert()
                return make_response(
                    jsonify(
                        {
                            "success": True,
                            "message": "User successfully created",
                            "new_author_id": new_user.id,
                            "new_username": new_user.username.format(),
                        }
                    ),
                    201,
                )

            return make_response(
                jsonify({"success": False, "message": "Password must match"}),
                400,
            )
        except Exception as e:
            print(e)
            abort(500)


@auth_bp.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()

    if data is None:
        abort(422)
    try:
        username_or_email = data.get("usernameOrEmail").strip()
        password = data.get("password").strip()

        check_by_username_or_email = User.query.filter(
            (User.user_email == username_or_email)
            | (User.username == username_or_email)
        ).one()
        print(check_by_username_or_email)
        if check_by_username_or_email and check_password_hash(
            check_by_username_or_email.password, password
        ):
            profile = {
                "id": check_by_username_or_email.id,
                "username": check_by_username_or_email.username.format(),
                "user_email": check_by_username_or_email.user_email.format(),
                "display_picture": check_by_username_or_email.display_picture.format(),
            }

            access_token = create_access_token(identity=profile)
            refresh_token = create_refresh_token(identity=profile)
            return jsonify(
                {
                    "success": True,
                    "message": f"Login successful, welcome {check_by_username_or_email.username.format()}",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                }
            )

        else:
            return make_response(
                jsonify(
                    {
                        "success": False,
                        "message": "Incorrect username/email or password",
                    }
                ),
                404,
            )
    except NoResultFound:
        return make_response(
            jsonify(
                {"success": False, "message": "Incorrect username/email or password"}
            ),
            404,
        )
    except Exception as e:
        print(e)
        abort(500)


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


@auth_bp.errorhandler(422)
def not_processable_error_handler(e):
    return handle_not_processable_error(e)
