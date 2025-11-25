from flask_sqlalchemy import SQLAlchemy

from .user import User
from .event import Event
from .comment import Comment
from .rsvp import RSVP

from config import db  # or however you import db
