from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.db import db


class Instructor(UserMixin, db.Model):
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False)
    surname = db.Column(db.String(50),
                        nullable=False)
    email = db.Column(db.String(120),
                      unique=True,
                      nullable=False)
    phone = db.Column(db.String(15),
                      unique=True,
                      nullable=False)
    password_hash = db.Column(db.String(512),
                              nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)  # NEW

    # convenience helpers
    def set_password(self, plaintext):
        self.password_hash = generate_password_hash(plaintext)

    def check_password(self, plaintext):
        return check_password_hash(self.password_hash, plaintext)

    def __repr__(self):
        return f"<Instructor {self.name}>"


class Slide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    image = db.Column(db.String(120))  # filename stored in static/images/nauka
    order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    order = db.Column(db.Integer, default=0)      # ← NEW
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(120))  # filename stored in static/images/cennik
    is_active = db.Column(db.Boolean, default=True)


class GalleryImage(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    filename  = db.Column(db.String(120), nullable=False)   # 01_galeria.jpg …
    alt       = db.Column(db.String(120))                   # "plac manewrowy" / "sala wykładowa"
    order     = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)


