
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import os

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

# ------------------------------------------------------------------------- #
@app.route('/')
def index():
    slides = Slide.query.filter_by(is_active=True).order_by(Slide.order).all()
    categories = Category.query.filter_by(is_active=True).all()

    hero_text = (
        "Dbamy o Twój komfort<br><br>"
        "Wszystkie pojazdy w naszej flocie są klimatyzowane, "
        "a instruktorzy dbają o przyjazną atmosferę na zajęciach."
    )

    return render_template(
        'index.html',
        slides=slides,
        categories=categories,
        hero_text=hero_text,
    )

if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
