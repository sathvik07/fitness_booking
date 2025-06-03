from sqlalchemy.orm import Session
from typing import List

from models import FitnessClass, Booking
from schemas import BookingRequest, FitnessClassOut, BookingOut
from utils import convert_ist_to_timezone


def get_all_classes(db: Session, timezone: str = "Asia/Kolkata") -> List[FitnessClassOut]:
    classes = db.query(FitnessClass).all()
    result = []

    for c in classes:
        result.append(FitnessClassOut(
            id=c.id,
            name=c.name,
            instructor=c.instructor,
            available_slots=c.available_slots,
            datetime=convert_ist_to_timezone(c.datetime, timezone)
        ))
    return result


def book_class(db: Session, data: BookingRequest) -> Booking:
    fitness_class = db.query(FitnessClass).filter(FitnessClass.id == data.class_id).first()

    if not fitness_class:
        raise ValueError("Class not found")

    if fitness_class.available_slots < 1:
        raise ValueError("No slots available for this class")

    booking = Booking(
        class_id=data.class_id,
        client_name=data.client_name,
        client_email=data.client_email
    )

    fitness_class.available_slots -= 1

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking


def get_user_bookings(db: Session, email: str) -> List[Booking]:
    return db.query(Booking).filter(Booking.client_email == email).all()
