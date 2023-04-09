from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from models.user import User, users_schema, user_schema
from flask import Blueprint, request, make_response, jsonify
from flask_bcrypt import generate_password_hash
from errors import (
    handle_bad_request,
    handle_not_processable_error,
    handle_unauthorized,
    handle_forbidden,
    handle_not_found,
    handle_method_not_allowed,
    handle_internal_server_error,
    handle_no_content,
)
from json import JSONDecodeError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import TimeoutError, IntegrityError
from utils import role_required

users_bp = Blueprint(
    "users",
    __name__,
    url_prefix="/users",
)


@users_bp.route("/", methods=["GET"])
@jwt_required()
@role_required("admin")
def fetch_all_users():
    """get all users from database"""
    try:
        users = User.query.order_by(User.username).all()
        if not users:
            return handle_no_content("No users currently")
        return make_response(
            jsonify({"users": users_schema.dump(users), "total_users": len(users)}), 200
        )

    except Exception as e:
        print(e)
        return internal_server_error_handler(
            "something went wrong please try again later"
        )


@users_bp.route("/user/<id>", methods=["GET"])
@jwt_required()
def fetch_specific_user(id):
    """get specific user from database"""
    user = User.query.get(str(id).strip())
    if not user:
        return not_found_handler("User not found")
    try:
        return make_response(jsonify({"user": user_schema.dump(user)}), 200)

    except Exception as e:
        print(e)
        return internal_server_error_handler(
            "something went wrong please try again later"
        )


@users_bp.route("/user/<id>", methods=["PUT"])
@jwt_required()
def update_specific_user(id):
    """update user details in database"""
    data = request.get_json()
    if not data:
        return handle_not_processable_error("")
    user_to_be_updated = User.query.get_or_404(str(id).strip())
    try:
        new_username = data.get("username")
        new_user_email = data.get("userEmail")
        new_display_picture = data.get("displayPicture")
        new_role = data.get("role")
        new_password = (
            generate_password_hash(data.get("password").strip()).decode("utf-8")
            if data.get("password")
            else None
        )

        user_to_be_updated.update(
            new_username, new_display_picture, new_user_email, new_password, new_role
        )
        return make_response(
            jsonify(
                {"success": True, "updated_user": user_schema.dump(user_to_be_updated)}
            ),
            200,
        )
    except JSONDecodeError:
        return handle_not_processable_error("")
    except IntegrityError:
        return handle_not_processable_error("")
    except ValidationError:
        return handle_not_processable_error("")
    except TimeoutError:
        return internal_server_error_handler(
            "something went wrong please try again later"
        )
    except Exception as e:
        return internal_server_error_handler(
            "something went wrong please try again later"
        )


@users_bp.route("/user/<id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
def delete_user(id):
    """delete a user from the database"""
    user_to_be_deleted = User.query.get_or_404(str(id).strip())
    try:
        user_to_be_deleted.delete()
        return make_response(
            jsonify({"success": True, "message": "User deleted successfully"}), 200
        )
    except NoResultFound:
        return handle_not_found("User not found")
    except Exception as e:
        print(e)
        return internal_server_error_handler(
            "something went wrong please try again later"
        )


@users_bp.errorhandler(400)
def bad_request_handler(e):
    return handle_bad_request("")


@users_bp.errorhandler(401)
def unauthorized_handler(e):
    return handle_unauthorized("")


@users_bp.errorhandler(403)
def forbidden_handler(e):
    return handle_forbidden("")


@users_bp.errorhandler(404)
def not_found_handler(e):
    return handle_not_found("")


@users_bp.errorhandler(405)
def method_not_allowed_handler(e):
    return handle_method_not_allowed("")


@users_bp.errorhandler(500)
def internal_server_error_handler(e):
    return handle_internal_server_error("")
