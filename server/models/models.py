from datetime import datetime
from exts import db
from uuid import uuid4
import shortuuid
from sqlalchemy.dialects.postgresql import UUID


def gen_post_id():
    return shortuuid.uuid()


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
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def insert(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def update(self, username=None, user_email=None, password=None) -> None:
        if username:
            self.username = username.strip()
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
        }

    def __repr__(self):
        return f"User('{str(self.id)}', '{self.username}', '{self.password}', '{self.user_email}')"


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
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=False)

    def insert(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def update(self, title=None, post_content=None) -> None:
        if title:
            self.title = title.strip()
        if post_content:
            self.post_content = post_content.strip()
        db.session.commit()

    def format(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "date_posted": self.date_posted,
            "post_content": self.post_content,
            "user_id": self.user_id,
        }

    def __repr__(self):
        return f"Post('{str(self.id)}', '{self.title}', '{self.date_posted}', '{self.post_content}')"
