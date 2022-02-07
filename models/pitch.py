from db import db
from datetime import date
from sqlalchemy.orm import relationship
from .user import User

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255))
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime(), default=date.today())
    pitch = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    user = relationship("User", backref="pitches")

    def __repr__(self):
        return f'Pitch {self.category}'