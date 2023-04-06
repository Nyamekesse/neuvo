from sqlalchemy import CheckConstraint
from exts import db, marshmallow
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import fields, pre_load
from models.post import PostsSchema

"""
class Users:
    id: String primary_key=True unique=True default=gen_uuid
    username: String(20) unique=True nullable=False
    user_email: String(120) unique=True nullable=False
    password: String(60) nullable=False
    profile_image: String(120) nullable=True default='default.jpg'
"""


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(36), primary_key=True, unique=True, default=str(uuid4()))
    username = db.Column(db.String(20), unique=True, nullable=False)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    display_picture = db.Column(db.String, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(10), nullable=False, default="user")
    posts = db.relationship("Post", backref="author", lazy=True)

    __table_args__ = (
        CheckConstraint(
            role.in_(["user", "creator", "admin"]),
            name="check_user_role",
        ),
    )

    def insert(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def update(
        self, username=None, display_picture=None, user_email=None, password=None
    ) -> None:
        if username:
            self.username = username
        if display_picture:
            self.display_picture = display_picture
        if user_email:
            self.user_email = user_email
        if password:
            self.password = password

        db.session.commit()

    def __repr__(self):
        return f"User('{str(self.id)}', '{self.username}', '{self.password}', '{self.user_email}','{self.display_picture}','{self.role}')"


class UserSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ("password", "posts")

    @pre_load
    def strip_whitespace(self, data, **kwargs):
        return {k: v.strip() if isinstance(v, str) else v for k, v in data.items()}

    id = fields.String(dump_only=True)
    # include the user's posts in the serialized output
    posts = fields.Nested(
        "PostsSchema", many=True, exclude=("author_id", "author_name")
    )


user_schema = UserSchema()
users_schema = UserSchema(many=True)
