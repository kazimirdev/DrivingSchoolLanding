"""
Run this once to create the DB tables and (optionally) insert seed data.
    python create_db.py
"""

from app import app, db, Slide, Category, GalleryImage

with app.app_context():
    db.drop_all()       # ← remove if you *don’t* want to wipe an existing DB
    db.create_all()

    images = []
    for i in range(1, 16):
        fname = f"{i:02d}_galeria.jpg"
        alt   = "sala wykładowa" if i >= 11 else "plac manewrowy"
        images.append(GalleryImage(filename=fname, alt=alt, order=i))
    db.session.add_all(images)

    # Uncomment the following lines to seed the database with initial data.
    """
    # ----------  SEED DATA  ------------------------------------------------
    slides = [
        Slide(order=1, title="Prawo jazdy kategorii A, A1, A2, B, B+E bez stresu",
              content=("Wszystkie pojazdy w naszej flocie są klimatyzowane, "
                       "a instruktorzy dbają o przyjazną atmosferę na zajęciach."),
              is_active=True),
        Slide(order=2, image="lesson1.jpg", is_active=True),
        Slide(order=3, title="Elastyczny grafik jazd",
              content="Dopasujemy godziny jazd do Twoich zajęć w szkole lub pracy.",
              is_active=True),
        Slide(order=4, image="lesson2.jpg", is_active=True),
    ]
    """

    categories = [
        Category(name="A2",            price=2200, is_active=True),
        Category(name="A",             price=2200, is_active=True),
        Category(name="B",             price=2200, is_active=True),
        Category(name="B (uczeń)",     price=2000, is_active=True,
                 description="Zniżka dla uczniów i studentów"),
        Category(name="A lub A2 + B",  price=4000, is_active=True),
    ]

    db.session.add_all(slides + categories)
    db.session.commit()

    print("✔ Database initialised and seeded.")
