from flask_restx import Resource, Namespace, fields
from models.models import Post
from flask_jwt_extended import jwt_required
from flask import request

post_ns = Namespace("post", description="Namespace for post")

create_post_model_data = post_ns.model(
    "Create New Post",
    {
        "title": fields.String(),
        "post_content": fields.String(),
        "user_id": fields.String(),
    },
)
posts_model = post_ns.model(
    "Posts",
    {
        "id": fields.String(),
        "title": fields.String(),
        "date_posted": fields.String(),
        "post_content": fields.String(),
        "user_id": fields.String(),
    },
)


@post_ns.route("/posts")
class PostsResource(Resource):
    @post_ns.marshal_list_with(posts_model)
    def get(self):
        """get all posts from database"""
        posts = Post.query.order_by(Post.title).all()
        return posts, 200

    @post_ns.marshal_with(posts_model)
    @post_ns.expect(create_post_model_data)
    @jwt_required()
    def post(self):
        """create a new post"""
        data = request.get_json()
        new_post = Post(
            title=data.get("title"),
            post_content=data.get("post_content"),
            user_id=data.get("user_id"),
        )
        new_post.insert()
        return new_post, 201


@post_ns.route("/posts/<id>")
class PostsResource(Resource):
    @post_ns.marshal_with(posts_model)
    def get(self, id):
        """get a specific post"""
        print(type(id))
        single_post = Post.query.get_or_404(id)
        return single_post

    @post_ns.marshal_with(posts_model)
    @jwt_required()
    def put(self, id):
        """update a specific post"""
        data = request.get_json()
        post_to_update = Post.query.get_or_404(id)
        post_to_update.update(data.get("title"), data.get("post_content"))
        return post_to_update, 200

    @post_ns.marshal_with(posts_model)
    @jwt_required()
    def delete(self, id):
        """delete a specific post"""
        post_to_delete = Post.query.get_or_404(id)
        post_to_delete.delete()

        return post_to_delete, 200
