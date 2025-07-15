"""
Run this once to create or reset the DB tables and seed them with initial data.

    python create_db.py
"""

from app import app, db, Slide, Category, GalleryImage

with app.app_context():
    # Drop existing tables so that running the script repeatedly always gives
    # the same deterministic outcome.  Remove the drop_all() call if you want
    # to preserve existing data.
    db.drop_all()
    db.create_all()

    # ----------  GALLERY IMAGES  ------------------------------------------
    images = []
    for i in range(1, 16):
        fname = f"{i:02d}_galeria.jpg"
        alt   = "sala wykładowa" if i >= 11 else "plac manewrowy"
        images.append(GalleryImage(filename=fname, alt=alt, order=i))

    # ----------  NAUKA SLIDES  --------------------------------------------
    slides = [
        Slide(order=1,
              title="Jazda – praktyka",
              content=("Godziny jazd ustalamy indywidualnie z kursantem, "
                       "tak aby bez stresu mógł łączyć szkolenie z obowiązkami."),
              image="jazda.jpg",
              is_active=True),

        Slide(order=2,
              title="Teoria – wykłady i e-learning",
              content=("Sala wyposażona jest w komputery oraz projektor multimedialny. "
                       "Cały materiał możesz powtarzać w domu dzięki dostępowi do platformy on-line."),
              image="teoria.jpg",
              is_active=True),

        Slide(order=3,
              title="Obsługa pojazdu",
              content=("Uczymy praktycznej obsługi i przygotowania pojazdu do jazdy. "
                       "Poznasz układ świateł, płyny eksploatacyjne i procedury bezpieczeństwa."),
              image="obsluga.jpg",
              is_active=True),
    ]

    # ----------  CATEGORIES  ----------------------------------------------
    categories = [
        Category(name="A2",            price=2200, is_active=True),
        Category(name="A",             price=2200, is_active=True),
        Category(name="B",             price=2200, is_active=True),
        Category(name="B (uczeń)",     price=2000, is_active=True,
                 description="Zniżka dla uczniów i studentów"),
        Category(name="A lub A2 + B",  price=4000, is_active=True),
    ]

    db.session.add_all(images + slides + categories)
    db.session.commit()

    print("✔ Database initialised and seeded.")
