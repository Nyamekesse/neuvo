from psycopg2 import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, make_response
from models.post import Post
from models.saved_posts import SavedPost, saved_post_schema
from errors import (
    handle_not_processable_error,
    handle_unauthorized,
    handle_not_found,
    handle_method_not_allowed,
    handle_internal_server_error,
)

save_post_bp = Blueprint(
    "saved_posts",
    __name__,
    url_prefix="/save_post",
)


@save_post_bp.route("/<post_id>/save", methods=["POST"])
@jwt_required
def save_post(post_id):
    user = get_jwt_identity()
    user_id = user.id
    # Check if post exists
    post = Post.query.get_or_404(id=post_id)

    # Check if post is already saved
    saved_post = SavedPost.query.filter_by(user_id=user_id, post_id=post_id).first()
    try:
        if saved_post:
            saved_post.delete()
            return (
                jsonify(
                    {
                        "success": True,
                    }
                ),
                204,
            )

        # Create new saved post
        new_saved_post = SavedPost(user_id=user_id, post_id=post_id)
        new_saved_post.insert()
        return make_response(
            jsonify(
                {
                    "success": True,
                    "saved_post": saved_post_schema.dump(new_saved_post),
                }
            ),
            201,
        )

    except IntegrityError:
        new_saved_post.rollback_session()
        return handle_internal_server_error("Something went wrong, please try again")
    except Exception as e:
        new_saved_post.rollback_session()
        return handle_internal_server_error("Something went wrong, please try again")


@save_post_bp.errorhandler(404)
def not_found_handler(e):
    return handle_not_found("the requested resource was not found")


@save_post_bp.errorhandler(500)
def internal_server_error_handler(e):
    return handle_internal_server_error("something went wrong please try again later")


@save_post_bp.errorhandler(405)
def method_not_allowed_handler(e):
    return handle_method_not_allowed()


@save_post_bp.errorhandler(401)
def unauthorized_handler(e):
    return handle_unauthorized()
