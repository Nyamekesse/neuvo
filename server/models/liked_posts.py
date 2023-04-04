import datetime
from exts import db, gen_short_id, marshmallow
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import fields


class LikedPost(db.Model):
    __tablename__ = "liked_posts"
    id = db.Column(db.String(22), primary_key=True, unique=True, default=gen_short_id)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    liked_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def insert(self) -> None:
        db.session.add(self)
        db.session.commit()

    def rollback_session(self) -> None:
        db.session.rollback()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"LikedPost('{self.id}', '{self.user_id}', '{self.post_id}', '{self.liked_at}')"


class LikedPostSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = LikedPost

    id = fields.String(required=True)
    user_id = fields.Integer(required=True)
    post_id = fields.Integer(required=True)
    liked_at = fields.DateTime(required=True)


liked_post_schema = LikedPostSchema()
