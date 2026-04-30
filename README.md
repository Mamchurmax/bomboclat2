# bomboclat2 / airbnb-flask-app

This project is a Flask-based web application that provides Airbnb-like functionality: listings, amenities, bookings, reviews, categories, photos, payments, messages and user management.

## Quickstart (local)

1. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

2. Set environment variables and run migrations:

```bash
export FLASK_APP=app:create_app
# Optionally: export DATABASE_URL=postgresql://user:pass@host:5432/dbname
flask db upgrade
flask run
```

3. Open Swagger UI at: [http://localhost:5000/apidocs/](http://localhost:5000/apidocs/)

## API Endpoints

### Listings
- `GET /listings/` — list listings
- `POST /listings/` — create listing
- `GET /listings/<id>` — get listing
- `PUT /listings/<id>` — update listing
- `DELETE /listings/<id>` — delete listing

### Amenities
- `GET /amenities/` — list amenities
- `POST /amenities/` — create amenity

### Users
- `POST /users/register` — register
- `POST /users/login` — login
- `GET /users/<id>` — get user
- `PUT /users/<id>` — update user
- `DELETE /users/<id>` — delete user

### Bookings
- `GET /bookings/` — list bookings
- `POST /bookings/` — create booking
- `GET /bookings/<id>` — get booking
- `PUT /bookings/<id>` — update booking
- `DELETE /bookings/<id>` — delete booking

### Reviews
- `GET /reviews/` — list reviews
- `POST /reviews/` — create review
- `GET /reviews/<id>` — get review
- `PUT /reviews/<id>` — update review
- `DELETE /reviews/<id>` — delete review

### Categories
- `GET /categories/` — list categories
- `POST /categories/` — create category
- `GET /categories/<id>` — get category
- `PUT /categories/<id>` — update category
- `DELETE /categories/<id>` — delete category

### Photos
- `GET /photos/` — list photos
- `POST /photos/` — create photo
- `GET /photos/<id>` — get photo
- `PUT /photos/<id>` — update photo
- `DELETE /photos/<id>` — delete photo

### Payments
- `GET /payments/` — list payments
- `POST /payments/` — create payment
- `GET /payments/<id>` — get payment
- `PUT /payments/<id>` — update payment
- `DELETE /payments/<id>` — delete payment

### Messages
- `GET /messages/` — list messages
- `POST /messages/` — create message
- `GET /messages/<id>` — get message
- `PUT /messages/<id>` — update message
- `DELETE /messages/<id>` — delete message

## Database Tables (11)

| # | Table | Description |
|---|-------|-------------|
| 1 | users | User accounts |
| 2 | listings | Property listings |
| 3 | amenities | Amenities (WiFi, Pool, etc.) |
| 4 | listing_amenities | M2M: listings ↔ amenities |
| 5 | listing_categories | M2M: listings ↔ categories |
| 6 | bookings | Reservations |
| 7 | reviews | User reviews for listings |
| 8 | categories | Listing categories |
| 9 | photos | Listing photos |
| 10 | payments | Booking payments |
| 11 | messages | User-to-user messages |

## Project Structure

- `app/` — application code (controllers, services, models, repositories, schemas)
- `migrations/` — Alembic database migrations
- `tests/` — unit tests

## Deployment

- Set `DATABASE_URL` for production (Postgres recommended).
- Provide `SECRET_KEY` environment variable.
- Production: `gunicorn -w 4 -b 0.0.0.0:5000 'app:create_app()'`
- Docker: `Dockerfile` included.

## Testing

```bash
pytest
```

## License

MIT
