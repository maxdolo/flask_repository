from datetime import datetime

from Blog import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_at = db.Column(db.DateTime, default=datetime.now)
    username = db.Column(db.String(12), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    exitposts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.email}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.now)
    titolo = db.Column(db.String(120), nullable=False)
    descrizione = db.Column(db.String(240))
    body = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f"Post('{self.id}, '{self.titolo}')"