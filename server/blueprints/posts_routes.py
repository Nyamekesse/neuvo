from sqlalchemy.exc import InvalidRequestError
from models.post import Post, posts_schema, post_schema
from flask_jwt_extended import jwt_required
from flask import Blueprint, request, jsonify, make_response
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from errors import (
    handle_not_processable_error,
    handle_unauthorized,
    handle_not_found,
    handle_method_not_allowed,
    handle_internal_server_error,
)

post_bp = Blueprint(
    "posts",
    __name__,
    url_prefix="/posts",
)

POSTS_PER_PAGE = 5


@post_bp.route("/", methods=["GET"])
def fetch_all_posts():
    """get all posts from database"""
    try:
        page = request.args.get("page", 1, type=int)
        paginated_posts = Post.query.order_by(Post.date_posted).paginate(
            page=page, per_page=POSTS_PER_PAGE
        )
        if page > paginated_posts.pages:
            return handle_not_found("Page not found")
        elif not paginated_posts.items:
            return handle_not_found("There are no posts available at the moment")

        return make_response(
            jsonify(
                {
                    "success": True,
                    "results": posts_schema.dump(paginated_posts.items),
                    "current_page": paginated_posts.page,
                    "number_of_pages": paginated_posts.pages,
                }
            ),
            200,
        )
    except InvalidRequestError as e:
        return handle_not_found("Page not found")


@post_bp.route("/new-post", methods=["POST"])
@jwt_required()
def create_new_post():
    """create a new post"""
    data = request.get_json()
    try:
        loaded_data = post_schema.load(data)
        new_post = Post(**loaded_data)
        new_post.insert()
        return (
            jsonify(
                {
                    "success": True,
                    "created_post": post_schema.dump(new_post),
                }
            ),
            200,
        )
    except ValidationError:
        return handle_not_processable_error("Values entered cannot be processable")
    except SQLAlchemyError:
        return handle_internal_server_error("Something went wrong, please tr again")


@post_bp.route("/post-details/<id>", methods=["GET"])
def fetch_post_details(id):
    """get a specific post"""

    single_post = Post.query.get_or_404(str(id).strip())
    return jsonify({"success": True, "post": post_schema.dump(single_post)})


@post_bp.route("/post/<id>", methods=["PUT"])
@jwt_required()
def update_post(id):
    """update a specific post"""
    data = request.get_json()
    post_to_update = Post.query.get_or_404(str(id).strip())
    try:
        loaded_data = post_schema.load(data, instance=post_to_update, partial=True)

        post_to_update.update(**loaded_data)
        return jsonify(
            {"success": True, "updated_post": post_schema.dump(post_to_update)}
        )
    except ValidationError:
        return handle_not_processable_error("Values entered cannot be processable")
    except SQLAlchemyError:
        return handle_internal_server_error(
            "Something went wrong, kindly try again later"
        )


@post_bp.route("/post/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    """delete a specific post"""
    post_to_delete = Post.query.get_or_404(str(id).strip())
    try:
        post_to_delete.delete()
        return (
            jsonify({"success": True, "message": "post successfully deleted"}),
            200,
        )
    except SQLAlchemyError:
        return handle_internal_server_error(
            "Something went wrong, kindly try again later"
        )


@post_bp.errorhandler(404)
def not_found_handler(e):
    return handle_not_found("the requested resource was not found")


@post_bp.errorhandler(500)
def internal_server_error_handler(e):
    return handle_internal_server_error("something went wrong please try again later")


@post_bp.errorhandler(405)
def method_not_allowed_handler(e):
    return handle_method_not_allowed()


@post_bp.errorhandler(401)
def unauthorized_handler(e):
    return handle_unauthorized()
