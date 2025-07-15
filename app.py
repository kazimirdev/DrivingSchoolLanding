from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configure your database URI. Example with SQLite:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///osk.db'
db = SQLAlchemy(app)

# --- MODELS --------------------------------------------------------------- #
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


# ------------------------------------------------------------------------- #


@app.context_processor
def inject_now():
    """Make `now()` usable in every template."""
    return {"now": datetime.utcnow}
@app.route('/')
def index():
    slides         = Slide.query.filter_by(is_active=True).order_by(Slide.order).all()
    categories     = Category.query.filter_by(is_active=True).all()
    gallery_images = (GalleryImage.query
                      .filter_by(is_active=True)
                      .order_by(GalleryImage.order)
                      .all())

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

