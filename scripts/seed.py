from app import app, db
from src.models import Instructor, Service

with app.app_context():
    db.create_all()
    db.session.add_all([
        Instructor(name="Barbara",
                   surname="Wysocka",
                   email="mail1@example.com",
                   phone="000000001",
                   password_hash="password1"),
        Instructor(name="Józef",
                   surname="Wysocki",
                   email="mail2@example.com",
                   phone="604523540",
                   password_hash="password2"),
        Service(name="Kategoria A1",
                price=2000.0,
                description="Kategoria A1 kursu, praktyczna część kursu odbywaja się na Romet 125.",
                is_active=False),
        Service(name="Kategoria A2",
                price=2200.0,
                description="Kategoria A2 kursu, praktyczna część kursu odbywaja się na Suzuki GS500."),
        Service(name="Kategoria A",
                price=2500.0,
                description="Kategoria A kursu, praktyczna część kursu odbywaja się na Suzuki Gladius 650."),
        Service(name="Kategoria B",
                price=2200.0,
                description="Kategoria B kursu, praktyczna część kursu odbywaja się na Citroen C3."),
        Service(name="Kategoria B (uczeń lub student)",
                price=2000.0,
                description="Kategoria B kursu, praktyczna część kursu odbywaja się na Citroen C3. Zniżka dla uczniów lub studentów."),
        Service(name="Kategoria B + E",
                price=3000.0,
                description="Kategoria B + E kursu, praktyczna część kursu odbywaja się na Citroen C3 z przyczepą.",
                is_active=False),
        Service(name="Kategoria A lub A2 + B (kombo)",
                price=4000.0,
                description="Połaczenie kursu kategorii A lub A2 i B.")])
    db.session.commit()
