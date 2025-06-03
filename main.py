from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import engine, get_db
import models
import crud
from schemas import FitnessClassOut, BookingRequest, BookingOut

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fitness Booking API")


@app.get("/")
def root():
    return {"message": "Fitness Booking API running!"}

@app.get("/classes", response_model=list[FitnessClassOut])
def read_classes(timezone: str = Query("Asia/Kolkata"), db: Session = Depends(get_db)):
    try:
        return crud.get_all_classes(db, timezone)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/book", response_model=BookingOut)
def book_class(data: BookingRequest, db: Session = Depends(get_db)):
    try:
        return crud.book_class(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/bookings", response_model=list[BookingOut])
def read_bookings(email: str = Query(...), db: Session = Depends(get_db)):
    return crud.get_user_bookings(db, email)
