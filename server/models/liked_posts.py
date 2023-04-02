import datetime
from exts import db, gen_short_id
from sqlalchemy.dialects.postgresql import UUID


class LikedPost(db.Model):
    __tablename__ = "liked_posts"
    id = db.Column(db.String(22), primary_key=True, unique=True, default=gen_short_id)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    liked_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"LikedPost('{self.id}', '{self.user_id}', '{self.post_id}', '{self.liked_at}')"
