from fastapi.testclient import TestClient
from main import app
import seed_data

client = TestClient(app)


def setup_module(module):
    print("\n🔄 Seeding database with test fitness classes...")
    seed_data.seed_classes()
    print("✅ Seed complete.\n")


def test_get_classes():
    print("▶️ Testing: GET /classes")
    response = client.get("/classes")
    assert response.status_code == 200
    data = response.json()
    print(f"📦 Found {len(data)} classes")
    assert isinstance(data, list)
    assert len(data) >= 1
    print("✅ GET /classes passed.\n")


def test_successful_booking():
    print("▶️ Testing: POST /book (successful booking)")
    response = client.post("/book", json={
        "class_id": 1,
        "client_name": "Test User",
        "client_email": "test@example.com"
    })
    assert response.status_code == 200
    data = response.json()
    print(f"🎫 Booking created for {data['client_name']} with email {data['client_email']}")
    assert data["client_email"] == "test@example.com"
    assert data["class_id"] == 1
    print("✅ POST /book passed.\n")


def test_overbooking():
    print("▶️ Testing: POST /book (overbooking scenario)")

    # Simulate a full class
    from database import SessionLocal
    from models import FitnessClass
    db = SessionLocal()
    fc = db.query(FitnessClass).filter(FitnessClass.id == 2).first()
    fc.available_slots = 0
    db.commit()
    db.close()
    print("⚠️ Simulated class with 0 available slots.")

    response = client.post("/book", json={
        "class_id": 2,
        "client_name": "John Doe",
        "client_email": "john@example.com"
    })
    assert response.status_code == 400
    assert "No slots available" in response.text
    print("✅ Overbooking correctly prevented.\n")


def test_get_bookings_by_email():
    print("▶️ Testing: GET /bookings?email=test@example.com")
    response = client.get("/bookings?email=test@example.com")
    assert response.status_code == 200
    data = response.json()
    print(f"📨 Found {len(data)} bookings for test@example.com")
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["client_email"] == "test@example.com"
    print("✅ GET /bookings passed.\n")
