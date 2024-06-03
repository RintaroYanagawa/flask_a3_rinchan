from todo import db
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from uuid_extensions import uuid7str
from todo.models.todos import Todos


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(CHAR(36), primary_key=True, nullable=False)
    public_id = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        server_default=db.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )

    todos = relationship("Todos")

    def __init__(self, public_id, password, name):
        self.id = uuid7str()
        self.public_id = public_id
        self.password = password
        self.name = name

    def __repr__(self):
        return "<Users public_id:{} password:{} name:{} created_at:{} updated_at:{}>".format(
            self.public_id, self.password, self.name, self.created_at, self.updated_at
        )
