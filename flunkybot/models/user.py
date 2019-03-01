"""The sqlite model for a user."""
from flunkybot.db import base
from sqlalchemy import (
    BigInteger,
    Integer,
    Boolean,
    Column,
    DateTime,
    String,
    func,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship


class User(base):
    """The model for a user."""

    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True)
    username = Column(String)

    rating = Column(Integer)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
