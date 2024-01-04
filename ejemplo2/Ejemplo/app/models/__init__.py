from .. import db

class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    lastName = db.Column(db.String(30))


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))