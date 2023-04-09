from psycopg2 import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, make_response
from models.post import Post
from models.saved_posts import SavedPost, saved_post_schema
from sqlalchemy.orm.exc import NoResultFound
from errors import (
    handle_unauthorized,
    handle_not_found,
    handle_method_not_allowed,
    handle_internal_server_error,
)

save_post_bp = Blueprint(
    "saved_post",
    __name__,
)


@save_post_bp.route("/<post_id>/save", methods=["POST"])
@jwt_required
def save_post(post_id):
    user = get_jwt_identity()
    user_id = user.id

    post = Post.query.get_or_404(id=post_id)

    saved_post = SavedPost.query.filter_by(user_id=user_id, post_id=post_id).first()
    try:
        if saved_post:
            saved_post.delete()
            return make_response(
                jsonify({"success": True, "message": "Post successfully unsaved"}),
                204,
            )

        new_saved_post = SavedPost(user_id=user_id, post_id=post_id)
        new_saved_post.insert()
        return make_response(
            jsonify(
                {
                    "success": True,
                    "message": "Post successfully saved",
                    "saved_post": saved_post_schema.dump(new_saved_post),
                }
            ),
            201,
        )

    except NoResultFound:
        return handle_not_found("")
    except IntegrityError:
        new_saved_post.rollback_session()
        return handle_internal_server_error("Something went wrong, please try again")
    except Exception as e:
        new_saved_post.rollback_session()
        return handle_internal_server_error("Something went wrong, please try again")


@save_post_bp.errorhandler(404)
def not_found_handler(e):
    return handle_not_found("")


@save_post_bp.errorhandler(500)
def internal_server_error_handler(e):
    return handle_internal_server_error("")


@save_post_bp.errorhandler(405)
def method_not_allowed_handler(e):
    return handle_method_not_allowed("")


@save_post_bp.errorhandler(401)
def unauthorized_handler(e):
    return handle_unauthorized("")
