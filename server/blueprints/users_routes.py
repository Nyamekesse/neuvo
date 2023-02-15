from flask_jwt_extended import jwt_required
from models.models import User
from flask import Blueprint, request

users_blueprint = Blueprint(
    "users", __name__, url_prefix="/users", description="Blueprint for users"
)


@users_blueprint.route("/")
def get():
    """get all users from database"""
    users = User.query.order_by(User.username).all()
    return users, 200


@users_blueprint.route("/<id>")
@jwt_required()
def get(id):
    """get specific user from database"""
    user = User.query.get_or_404(id)
    return user, 200


@users_blueprint.route("/user/<id>")
@jwt_required()
def put(id):
    """update user details in database"""
    data = request.get_json()
    user_to_be_updated = User.query.get_or_404(id)
    user_to_be_updated.update(
        data.get("username"),
        data.get("user_email"),
        data.get("password"),
        data.get("profile_image"),
    )
    return user_to_be_updated, 200


@users_blueprint.route("/user/<id>")
@jwt_required()
def delete(id):
    """delete a user from the database"""
    user_to_be_deleted = User.query.get_or_404(id)
    user_to_be_deleted.delete()
    return user_to_be_deleted, 200
