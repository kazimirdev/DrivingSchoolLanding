import os, secrets

from datetime import datetime

from flask import Flask, render_template

from src.db import db
from src.models import Slide, Category, GalleryImage

app = Flask(__name__,
            static_folder='static',
            template_folder='templates',
            static_url_path='/static')

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or secrets.token_hex(32)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL",
    "sqlite:///db.sqlite3")  # Default to SQLite if no DATABASE_URL is set
db.init_app(app)

import src.admin

@app.context_processor
def inject_now():
    return {"now": datetime.now}
@app.route('/')
def index():
    slides = Slide.query.filter_by(is_active=True).order_by(Slide.order).all()
    categories = Category.query.filter_by(is_active=True).order_by(Category.order).all()
    gallery_images = (
        GalleryImage.query.filter_by(
            is_active=True).order_by(GalleryImage.order).all())

    hero_text = (
        "Indywidualnie zajęcią zgodnie z twoim trybem życia.<br> "
        "Instruktorzy dbają o przyjazną atmosferę na zajęciach."
    )
    return render_template(
        'index.html',
        slides=slides,
        categories=categories,
        gallery_images=gallery_images,   #  <<–– NEW
        hero_text=hero_text,
    )

if __name__ == '__main__':
    app.run(debug=True)

