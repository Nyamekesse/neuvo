from datetime import datetime
from exts import db, marshmallow
import shortuuid
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import fields, pre_load


def gen_post_id():
    return shortuuid.uuid()


"""
class Post:
    id: String primary_key=True unique=True default=gen_uuid
    title: String(100) nullable=False
    date_posted: DateTime nullable=False default=gen_date
    post_content: Text nullable=False
"""


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.String(22), primary_key=True, unique=True, default=gen_post_id)

    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    post_content = db.Column(db.Text, nullable=False)
    post_image = db.Column(db.String, nullable=False)
    author_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=False)
    author_name = db.Column(db.String(20), nullable=False)

    def insert(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def update(self, title=None, post_content=None, post_image=None) -> None:
        if title:
            self.title = title.strip()
        if post_content:
            self.post_content = post_content.strip()
        if post_image:
            self.post_image = post_image.strip()
        db.session.commit()

    # def format(self):
    #     return {
    #         "id": str(self.id),
    #         "title": self.title,
    #         "date_posted": self.date_posted,
    #         "post_content": self.post_content,
    #         "post_image": self.post_image,
    #         "author_id": self.author_id,
    #         "author_name": self.author_name,
    #     }

    def __repr__(self):
        return f"Post('{str(self.id)}', '{self.title}', '{self.date_posted}', '{self.post_content}','{self.post_image}'),'{self.author_id}','{self.author_name}'"


class PostsSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Post

    @pre_load
    def strip_whitespace(self, data, **kwargs):
        return {k: v.strip() if isinstance(v, str) else v for k, v in data.items()}

    id = fields.String(dump_only=True)
    author_id = fields.UUID()


post_schema = PostsSchema()
posts_schema = PostsSchema(many=True)
