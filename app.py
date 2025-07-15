from datetime import datetime

from flask import Flask, render_template

from src.db import db
from src.models import Slide, Category, GalleryImage

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///osk.db'
db.init_app(app)

@app.context_processor
def inject_now():
    return {"now": datetime.now}
@app.route('/')
def index():
    slides = Slide.query.filter_by(is_active=True).order_by(Slide.order).all()
    categories = Category.query.filter_by(is_active=True).all()
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
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)

