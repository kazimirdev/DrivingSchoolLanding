from src.db import db

class Instructor(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
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

    def __repr__(self):
        return f"<Instructor {self.name}>"


class Student(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(50),
                     nullable=False)
    surname = db.Column(db.String(50),
                        nullable=False)
    pkk = db.Column(db.Integer,
                    unique=True,
                    nullable=False)
    email = db.Column(db.String(120),
                      unique=True,
                      nullable=False)
    phone = db.Column(db.String(9),
                      unique=True,
                      nullable=False)
    password_hash = db.Column(db.String(512),
                              nullable=False)
    purchases = db.relationship('Purchase',
                                backref='student',
                                lazy=True)

    def __repr__(self):
        return f"<Student {self.name}>"

class Service(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(50),
                     nullable=False)
    price = db.Column(db.Float,
                      nullable=False)
    description = db.Column(db.String(2048),
                            nullable=True)
    images_url = db.Column(db.String(2048),
                           nullable=True)
    is_active = db.Column(db.Boolean,
                          default=True,
                          nullable=False)

    def __repr__(self):
        return f"<Service {self.name}>"


class Purchase(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    student_id = db.Column(db.Integer,
                           db.ForeignKey('student.id'),
                           nullable=False)
    service_id = db.Column(db.Integer,
                           db.ForeignKey('service.id'),
                           nullable=False)
    date = db.Column(db.DateTime,
                     nullable=False)
    time = db.Column(db.Time,
                     nullable=False)

    def __repr__(self):
        return f"<Purchase {self.id} by Student {self.student_id} for Service {self.service_id}>"



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
