import math
from flask_restx import Resource, Namespace, fields
from models.models import Post
from flask_jwt_extended import jwt_required
from flask import request, jsonify, abort


post_ns = Namespace("posts", description="Namespace for post")

create_post_model_data = post_ns.model(
    "Create New Post",
    {
        "title": fields.String(),
        "post_content": fields.String(),
        "user_id": fields.String(),
    },
)


POSTS_PER_PAGE = 5


@post_ns.route("/", methods=["GET", "POST"])
class PostsResource(Resource):
    @staticmethod
    def paginate_display(page, queried_posts):
        """pagination"""

        start = (page - 1) * POSTS_PER_PAGE
        end = start + POSTS_PER_PAGE
        return [post.format() for post in queried_posts[start:end]]

    def get(self):
        """get all posts from database"""

        try:

            posts = Post.query.order_by(Post.title).all()
            number_of_all_posts = len(posts)
            page = request.args.get("page", 1, type=int)
            posts = self.paginate_display(page, posts)
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

    @post_ns.expect(create_post_model_data)
    @jwt_required()
    def post(self):
        """create a new post"""
        try:
            data = request.get_json()
            new_post = Post(
                title=data.get("title"),
                post_content=data.get("post_content"),
                user_id=data.get("user_id"),
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


@post_ns.route("/details", methods=["GET"])
class PostsResource(Resource):
    def get(self):
        """get a specific post"""
        try:
            id = request.args.get("id", type=str)
            single_post = Post.query.get_or_404(id)

            return jsonify({"success": True, "post": single_post.format()})

        except:
            abort(404)


@post_ns.route("/post", methods=["PUT", "DELETE"])
class PostsResource(Resource):
    @jwt_required()
    def put(self):
        """update a specific post"""
        id = request.args.get("id", type=str)
        data = request.get_json()
        post_to_update = Post.query.get_or_404(id)
        post_to_update.update(data.get("title"), data.get("post_content"))

        return jsonify({"success": True, "updated_post": post_to_update.format()})

    @jwt_required()
    def delete(self):
        """delete a specific post"""

        try:
            id = request.args.get("id", type=str)
            post_to_delete = Post.query.get_or_404(id)
            post_to_delete.delete()
            return (
                jsonify({"success": True, "deleted_post": post_to_delete.format()}),
            )
        except:
            abort(404)
