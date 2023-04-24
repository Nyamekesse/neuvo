from sqlalchemy.exc import InvalidRequestError
from models.post import Post, posts_schema, post_schema
from flask_jwt_extended import jwt_required
from flask import Blueprint, request, jsonify, make_response
from marshmallow import ValidationError
from sqlalchemy.orm.exc import NoResultFound
from errors import (
    handle_not_processable_error,
    handle_unauthorized,
    handle_not_found,
    handle_method_not_allowed,
    handle_internal_server_error,
    handle_no_content,
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
            return handle_no_content("No posts available at the moment")

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
    except InvalidRequestError:
        return handle_not_processable_error("")
    except Exception as e:
        return internal_server_error_handler(
            "something went wrong please try again later"
        )


@post_bp.route("/new-post", methods=["POST"])
# @jwt_required()
def create_new_post():
    """create a new post"""
    data = request.get_json()
    if not data:
        return handle_not_processable_error("")
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
        return handle_not_processable_error("")
    except Exception as e:
        return internal_server_error_handler(
            "something went wrong please try again later"
        )


@post_bp.route("/post-details/<id>", methods=["GET"])
def fetch_post_details(id):
    """get a specific post"""
    try:
        single_post = Post.query.get(str(id).strip())
        if not single_post:
            return handle_not_found("")
        return jsonify({"success": True, "post": post_schema.dump(single_post)})

    except Exception as e:
        print(e)
        return internal_server_error_handler(
            "something went wrong please try again later"
        )


@post_bp.route("/post/<id>", methods=["PUT"])
@jwt_required()
def update_post(id):
    """update a specific post"""
    data = request.get_json()
    if not data:
        return handle_not_processable_error("")
    post_to_update = Post.query.get_or_404(str(id).strip())
    try:
        loaded_data = post_schema.load(data, instance=post_to_update, partial=True)

        post_to_update.update(**loaded_data)
        return jsonify(
            {"success": True, "updated_post": post_schema.dump(post_to_update)}
        )
    except ValidationError:
        return handle_not_processable_error("")
    except Exception as e:
        return internal_server_error_handler(
            "something went wrong please try again later"
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
    except NoResultFound:
        return handle_not_found("")
    except Exception as e:
        return internal_server_error_handler(
            "something went wrong please try again later"
        )


@post_bp.route("/search")
def search():
    try:
        q = request.args.get("q")
        if not q:
            return handle_not_processable_error("")
        results = Post.query.whooshee_search(q).all()
        if not results:
            return handle_not_found("Your search query could not match any post")
        return jsonify({"success": True, "query": q, "results": posts_schema(results)})
    except Exception as e:
        print(e)
        return internal_server_error_handler(
            "something went wrong please try again later"
        )


@post_bp.errorhandler(404)
def not_found_handler(e):
    return handle_not_found("")


@post_bp.errorhandler(500)
def internal_server_error_handler(e):
    return handle_internal_server_error("")


@post_bp.errorhandler(405)
def method_not_allowed_handler(e):
    return handle_method_not_allowed("")


@post_bp.errorhandler(401)
def unauthorized_handler(e):
    return handle_unauthorized("")
