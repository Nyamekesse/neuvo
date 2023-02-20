from exts import db
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from exts import marshmallow
from flask_marshmallow import fields

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
    id = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid4)
    username = db.Column(db.String(20), unique=True, nullable=False)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    display_picture = db.Column(db.String, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

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
            self.username = username.strip()
        if display_picture:
            self.display_picture = display_picture.strip()
        if user_email:
            self.user_email = user_email.strip()
        if password:
            self.password = password

        db.session.commit()

    def format(self):
        return {
            "id": str(self.id),
            "username": self.username,
            "user_email": self.user_email,
            "password": self.password,
            "display_picture": self.display_picture,
        }

    def __repr__(self):
        return f"User('{str(self.id)}', '{self.username}', '{self.password}', '{self.user_email}','{self.display_picture}')"


class UserSchema(marshmallow.Schema):
    class Meta:
        fields = ("id", "username", "user_email", "display_picture", "posts")


user_schema = UserSchema()
users_schema = UserSchema(many=True)
