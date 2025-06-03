# ️Fitness Booking API

A simple Booking API for a fictional fitness studio offering Yoga, Zumba, and HIIT classes.

---

##  Features

- View all upcoming fitness classes
- Book a spot in a class
- View bookings by email
- Timezone support (default IST)
- Prevents overbooking and handles validations

---

##  Tech Stack

- Python 3.9+
- FastAPI
- SQLite (in-memory or file-based)
- SQLAlchemy
- Pydantic
- pytz (for timezone management)

---

##  Setup Instructions

1. **Clone the repo or unzip folder**
    ```bash
    git clone https://github.com/sathvik07/fitness_booking.git 
    cd fitness_booking
    ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
    ```
   
3. Seed the database with initial data (optional):
   ```bash
   python seed_data.py
   ```

4. **Run the API server**  
   ```bash
    uvicorn main:app --reload
    ```

5. **Access the API**
   Open your browser and go to `http://127.0.0.1:8000/docs` to view the API documentation and test endpoints.

6. **Test the API**
   Use tools like Postman or curl to test the endpoints. You can also use the Swagger UI at `/docs` to interact with the API.
