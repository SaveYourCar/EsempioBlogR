"""
Questo e il modello che rappresenta la tabella degli utenti,
con il tipo db.relationship() identifico un relazione con la tabella dei post,
di conseguenza all'interno della tabella post andro ad inserire la chiave primaria di User come chiave esterna
"""
from core.config import db


class User(db.Model):

    user_id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
