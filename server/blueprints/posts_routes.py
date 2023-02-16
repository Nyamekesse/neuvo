import math

from models.models import Post
from flask_jwt_extended import jwt_required
from flask import Blueprint, request, jsonify, abort

from errors import (
    handle_bad_request,
    handle_not_processable_error,
    handle_unauthorized,
    handle_forbidden,
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


def paginate_display(page, queried_posts):
    """pagination"""

    start = (page - 1) * POSTS_PER_PAGE
    end = start + POSTS_PER_PAGE
    return [post.format() for post in queried_posts[start:end]]


@post_bp.route("/", methods=["GET"])
def fetch_all_posts():
    """get all posts from database"""
    try:
        posts = Post.query.order_by(Post.title).all()
        number_of_all_posts = len(posts)
        page = request.args.get("page", 1, type=int)
        posts = paginate_display(page, posts)
        return jsonify(
            {
                "success": True,
                "results": posts,
                "current_page": request.args.get("page"),
                "number_of_pages": math.ceil(number_of_all_posts / POSTS_PER_PAGE),
            }
        )

    except:
        abort(400)


@post_bp.route("/new-post", methods=["POST"])
@jwt_required()
def create_new_post():
    """create a new post"""
    data = request.get_json()
    if data is None:
        abort(422)
    try:
        new_post = Post(
            title=data.get("title").strip(),
            post_content=data.get("post_content").strip(),
            user_id=data.get("user_id").strip(),
        )
        new_post.insert()
        return (
            jsonify(
                {
                    "success": True,
                    "created_post": new_post.format(),
                }
            ),
        )

    except:
        abort(401)


@post_bp.route("/post-details/<id>", methods=["GET"])
def fetch_post_details(id):
    """get a specific post"""
    if id is None:
        abort(422)
    single_post = Post.query.get_or_404(id)
    return jsonify({"success": True, "post": single_post.format()})


@post_bp.route("/post/<id>", methods=["PUT"])
@jwt_required()
def update_post():
    """update a specific post"""
    data = request.get_json()
    if not data or not id:
        abort(422)
    post_to_update = Post.query.get_or_404(str(id).strip())
    try:
        post_to_update.update(data.get("title"), data.get("post_content"))
        return jsonify({"success": True, "updated_post": post_to_update.format()})
    except Exception as e:
        print(e)
        abort(500)


@post_bp.route("/post/<id>", methods=["DELETE"])
@jwt_required()
def delete():
    """delete a specific post"""
    post_to_delete = Post.query.get_or_404(str(id).strip())
    try:
        post_to_delete.delete()
        return (
            jsonify({"success": True, "deleted_post": post_to_delete.format()}),
            200,
        )
    except Exception as e:
        print(e)
        abort(500)


@post_bp.errorhandler(400)
def bad_request_handler(e):
    return handle_bad_request(e)


@post_bp.errorhandler(401)
def unauthorized_handler(e):
    return handle_unauthorized(e)


@post_bp.errorhandler(403)
def forbidden_handler(e):
    return handle_forbidden(e)


@post_bp.errorhandler(404)
def not_found_handler(e):
    return handle_not_found(e)


@post_bp.errorhandler(405)
def method_not_allowed_handler(e):
    return handle_method_not_allowed(e)


@post_bp.errorhandler(422)
def not_processable_error_handler(e):
    return handle_not_processable_error(e)


@post_bp.errorhandler(500)
def internal_server_error_handler(e):
    return handle_internal_server_error(e)
