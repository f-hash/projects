from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()
from flask_login import UserMixin


class userlogin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # autoincrements
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(40), unique=True, nullable=False)

    def __repr__(self):  # you need this
        # self.username = username
        #      self.password = password
        return "<userlogin %r>" % self.username


class ratings(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    mov_id = db.Column(db.Integer, default=0)
    score = db.Column(db.Integer, default=0)
    comments = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, default=0)

    def __init__(self, mov_id, score, comments, user_id):  # you need this
        self.mov_id = mov_id
        self.score = score
        self.comments = comments
        self.user_id = user_id

    def __repr__(self):
        return self.comments

    def json(self):
        return {"comments": [comments.json() for comments in self.comments]}
