from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from models.models import User
from flask import request

user_ns = Namespace("users", description="Namespace for users")

users_model = user_ns.model(
    "Users",
    {
        "id": fields.String(),
        "username": fields.String(),
        "user_email": fields.String(),
        "avatar": fields.String(),
    },
)


@user_ns.route("/")
class UsersResource(Resource):
    @user_ns.marshal_list_with(users_model)
    def get(self):
        """get all users from database"""
        users = User.query.order_by(User.username).all()
        return users, 200


@user_ns.route("/<id>")
class UsersResource(Resource):
    @user_ns.marshal_with(users_model)
    @jwt_required()
    def get(self, id):
        """get specific user from database"""
        user = User.query.get_or_404(id)
        return user, 200

    @user_ns.marshal_with(users_model)
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

    @user_ns.marshal_with(users_model)
    @jwt_required()
    def delete(self, id):
        """delete a user from the database"""
        user_to_be_deleted = User.query.get_or_404(id)
        user_to_be_deleted.delete()
        return user_to_be_deleted, 200
