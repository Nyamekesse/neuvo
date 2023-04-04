from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, make_response
from models.post import Post
from models.liked_posts import LikedPost, liked_post_schema, LikedPost
from psycopg2 import IntegrityError
from errors import (
    handle_not_processable_error,
    handle_unauthorized,
    handle_not_found,
    handle_method_not_allowed,
    handle_internal_server_error,
)

like_post_bp = Blueprint(
    "liked_posts",
    __name__,
)


@like_post_bp.route("/<post_id>/like", methods=["POST"])
@jwt_required()
def like_post(post_id):
    user = get_jwt_identity()
    user_id = user.get("id")

    # Check if post exists
    post = Post.query.get_or_404(post_id)

    # Check if post is already liked
    liked_post = LikedPost.query.filter_by(user_id=user_id, post_id=post_id).first()
    try:
        if liked_post:
            # Delete the liked post
            liked_post.delete()
            return make_response(
                jsonify({"success": True}),
                204,
            )

        # Create new liked post
        new_liked_post = LikedPost(user_id=user_id, post_id=post_id)
        new_liked_post.insert()
        return make_response(
            jsonify(
                {
                    "success": True,
                    "liked_post": liked_post_schema.dump(new_liked_post),
                }
            ),
            201,
        )
    except IntegrityError:
        new_liked_post.rollback_session()
        return handle_internal_server_error("Something went wrong, please try again")
    except:
        new_liked_post.rollback_session()
        return handle_internal_server_error("Something went wrong, please try again")


@like_post_bp.errorhandler(404)
def not_found_handler(e):
    return handle_not_found("the requested resource was not found")


@like_post_bp.errorhandler(500)
def internal_server_error_handler(e):
    return handle_internal_server_error("something went wrong please try again later")


@like_post_bp.errorhandler(405)
def method_not_allowed_handler(e):
    return handle_method_not_allowed()


@like_post_bp.errorhandler(401)
def unauthorized_handler(e):
    return handle_unauthorized()
