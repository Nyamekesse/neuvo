from datetime import datetime
from exts import db
from uuid import uuid4
import json
from typing import Dict

def gen_uuid():
    return uuid4().hex
def gen_date():
    return datetime.utcnow()
"""
class Users:
    id: String primary_key=True unique=True default=gen_uuid
    username: String(20) unique=True nullable=False
    user_email: String(120) unique=True nullable=False
    password: String(60) nullable=False
    avatar: String(120) nullable=True default='default.jpg'
"""
class User(db.Model):
    id=db.Column(db.String(35), primary_key=True, unique=True, default=gen_uuid)
    username=db.Column(db.String(20), unique=True, nullable=False)
    user_email=db.Column(db.String(120), unique=True, nullable=False)
    password=db.Column(db.String(60), nullable=False)
    avatar=db.Column(db.String(30), nullable=False, default='default.jpg')
    posts=db.relationship('Post', backref='author', lazy=True)

    def display(self) -> Dict:
        return {
            'id': self.id,
            'username': self.username,
            'user_email': self.user_email,
            'avatar': self.avatar
        }

    def insert(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def update(self, username, user_email, password, avatar) -> None:
        self.username=username
        self.user_email=user_email
        self.password=password
        self.avatar=avatar
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.display())
"""
class Post:
    id: String primary_key=True unique=True default=gen_uuid
    title: String(100) nullable=False
    date_posted: DateTime nullable=False default=gen_date
    post_content: Text nullable=False
"""
class Post(db.Model):
    id=db.Column(db.String(35), primary_key=True, unique=True, default=gen_uuid)
    title=db.Column(db.String(100), nullable=False)
    date_posted=db.Column(db.DateTime, nullable=False, default=gen_date)
    post_content=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.String(35), db.ForeignKey('user.id'), nullable=False)

    def display(self) -> Dict:
        return {
            'id': self.id,
            'title': self.title,
            'date_posted': self.date_posted,
            'post_content': self.post_content
        }

    def insert(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def update(self, title, date_posted, post_content, avatar) -> None:
        self.title=title
        self.date_posted=date_posted
        self.post_content=post_content
        self.avatar=avatar
        db.session.commit()
    
    def __repr__(self):
        return json.dumps(self.display())
