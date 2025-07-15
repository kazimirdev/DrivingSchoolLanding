from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///school.db"
db = SQLAlchemy(app)

@app.route("/api/cennik")
def price_api():
    from src.models import Service
    services = Service.query.all()
    return {
        "services": [
            {
                "id": service.id,
                "name": service.name,
                "price": service.price,
                "description": service.description,
                "images_url": service.images_url
            } for service in services
        ]
    }

@app.route("/api/instructors")
def instructors_api():
    from src.models import Instructor
    instructors = Instructor.query.all()
    return {
        "instructors": [
            {
                "id": instructor.id,
                "name": instructor.name,
                "surname": instructor.surname,
                "email": instructor.email,
                "phone": instructor.phone
            } for instructor in instructors
        ]
    }


@app.route("/")
def index():
    services = price_api().get("services", [])
    instructors = instructors_api().get("instructors", [])
    return render_template("index.html",
                           services=services,
                           instructors=instructors)

