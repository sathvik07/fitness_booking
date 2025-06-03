from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, FitnessClass

Base.metadata.create_all(bind=engine)

def seed_classes():
    db: Session = SessionLocal()

    db.query(FitnessClass).delete()

    now = datetime.now()
    classes = [
        FitnessClass(
            name="Yoga",
            instructor="Aditi Sharma",
            datetime=(now + timedelta(days=1, hours=6)),
            total_slots=10,
            available_slots=10
        ),
        FitnessClass(
            name="Zumba",
            instructor="Rahul Mehta",
            datetime=(now + timedelta(days=2, hours=7)),
            total_slots=15,
            available_slots=15
        ),
        FitnessClass(
            name="HIIT",
            instructor="Sneha Patel",
            datetime=(now + timedelta(days=3, hours=8)),
            total_slots=12,
            available_slots=12
        ),
    ]

    db.add_all(classes)
    db.commit()
    db.close()
    print("✅ Seeded initial class data.")

if __name__ == "__main__":
    seed_classes()
