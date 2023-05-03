from datetime import datetime
from exts import db, marshmallow, whooshee
from utils import gen_short_id
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import fields, pre_load


"""
class Post:
    id: String primary_key=True unique=True default=gen_uuid
    title: String(100) nullable=False
    date_posted: DateTime nullable=False default=gen_date
    post_content: Text nullable=False
"""


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

    def insert(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()


class CategorySchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Category


category_schema = CategorySchema()


@whooshee.register_model("title", "post_content")  # expose fields for search
class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.String(22), primary_key=True, unique=True, default=gen_short_id)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    post_content = db.Column(db.Text, nullable=False)
    post_image = db.Column(db.String, nullable=False)
    author_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
    author_name = db.Column(db.String(20), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    category = db.relationship("Category", backref=db.backref("posts", lazy=True))

    def insert(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def update(
        self, title=None, post_content=None, post_image=None, category_id=None
    ) -> None:
        if title:
            self.title = title
        if post_content:
            self.post_content = post_content
        if post_image:
            self.post_image = post_image
        if category_id:
            self.category_id = category_id
        db.session.commit()

    def __repr__(self):
        return f"Post('{str(self.id)}', '{self.title}', '{self.date_posted}', '{self.post_content}','{self.post_image}'),'{self.author_id}','{self.author_name}'"


class PostSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        exclude = ("category_id",)

    @pre_load
    def strip_whitespace(self, data, **kwargs):
        return {k: v.strip() if isinstance(v, str) else v for k, v in data.items()}

    id = fields.String(dump_only=True)
    date_posted = fields.DateTime(dump_only=True)
    author_id = fields.String()
    category = fields.Nested(category_schema, only=("id", "name"))
    category_id = fields.Integer()


class UpdatePostSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        exclude = ("date_posted",)

    @pre_load
    def strip_whitespace(self, data, **kwargs):
        return {k: v.strip() if isinstance(v, str) else v for k, v in data.items()}

    id = fields.String(dump_only=True)
    title = fields.String(required=True)
    author_id = fields.String()
    category_id = fields.Integer()


post_schema = PostSchema()
update_post_schema = UpdatePostSchema()
posts_schema = PostSchema(many=True)
