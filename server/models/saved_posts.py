from datetime import datetime
from exts import db, gen_short_id, marshmallow
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import fields


class SavedPost(db.Model):
    __tablename__ = "saved_posts"
    id = db.Column(db.String(22), primary_key=True, unique=True, default=gen_short_id)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.String(22), db.ForeignKey("posts.id"), nullable=False)
    saved_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def insert(self) -> None:
        db.session.add(self)
        db.session.commit()

    def rollback_session(self) -> None:
        db.session.rollback()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"SavedPost('{self.id}', '{self.user_id}', '{self.post_id}'),'{self.saved_at}'"


class SavedPostSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = SavedPost

    id = fields.String(dump_only=True)
    user_id = fields.UUID(required=True)
    post_id = fields.String(required=True)
    saved_at = fields.DateTime(dump_only=True)


saved_post_schema = SavedPostSchema()
