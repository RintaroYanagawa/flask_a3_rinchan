from todo import db
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.sql import func
from uuid_extensions import uuid7str
from nanoid import generate


class Todos(db.Model):
    __tablename__ = "todos"
    id = db.Column(CHAR(36), primary_key=True, nullable=False)
    public_id = db.Column(CHAR(21), unique=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    contents = db.Column(db.String(500), nullable=False)
    limit = db.Column(db.DateTime, nullable=False)
    is_done = db.Column(db.Boolean, default=False)
    user_id = db.Column(
        "user_id",
        CHAR(36),
        db.ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"),
    )
    created_at = db.Column(
        db.DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        server_default=db.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )

    def __init__(self, title, contents, limit, user_id):
        self.id = uuid7str()
        self.public_id = generate()
        self.title = title
        self.contents = contents
        self.limit = limit
        self.user_id = user_id

    def __repr__(self):
        return "<Todos id:{} public_id:{} title:{} contents:{} limit:{} is_done:{} user_id:{} created_at:{} updated_at:{}>".format(
            self.id,
            self.public_id,
            self.title,
            self.contents,
            self.limit,
            self.is_done,
            self.user_id,
            self.created_at,
            self.updated_at,
        )
