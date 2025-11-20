<<<<<<< HEAD
# bomboclat2
=======
# airbnb-flask-app

Simple Flask app for listings, amenities and users. Contains services, repositories and SQLAlchemy models.

Quickstart (local):

1. Create virtualenv and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Set environment variables and run migrations (if using SQLite this is optional):

```bash
export FLASK_APP=app:create_app
# optionally: export DATABASE_URL=postgresql://user:pass@host:5432/dbname
flask db upgrade
flask run
```

3. API endpoints:

- `GET /listings/` — list listings
- `POST /listings/` — create listing
- `GET /listings/<id>` — get listing
- `PUT /listings/<id>` — update listing
- `DELETE /listings/<id>` — delete listing
- `GET /amenities/`, `POST /amenities/` — manage amenities
- `POST /users/register`, `POST /users/login` — user flows (currently in-memory user store)

Deployment notes:

- Configure `DATABASE_URL` environment variable for production (recommend Postgres).
- Add `SECRET_KEY` env var for Flask.
- You can run with Gunicorn in production: `gunicorn -w 4 -b 0.0.0.0:5000 'app:create_app()'` or use Docker (Dockerfile included).

CI/CD:

- Add a GitHub Actions workflow or provider-specific deploy pipeline to push changes to your VM or App Service.
# Airbnb Flask Application

This project is a web application built using Flask that mimics the functionality of Airbnb. It allows users to create, manage, and book listings, as well as manage amenities and user accounts.

## Project Structure

The project is organized into several directories and files:

# bomboclat2 / airbnb-flask-app

This project is a Flask-based web application that provides basic Airbnb-like functionality: listings, amenities and user management. The repo was developed as part of a course project and includes controllers, services, repositories and SQLAlchemy models.

## Quickstart (local)

1. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Set environment variables and run migrations (if using a database other than SQLite):

```bash
export FLASK_APP=app:create_app
# Optionally: export DATABASE_URL=postgresql://user:pass@host:5432/dbname
flask db upgrade
flask run
```

3. API endpoints (examples):

- `GET /listings/` — list listings
- `POST /listings/` — create listing
- `GET /listings/<id>` — get listing
- `PUT /listings/<id>` — update listing
- `DELETE /listings/<id>` — delete listing
- `GET /amenities/`, `POST /amenities/` — manage amenities
- `POST /users/register`, `POST /users/login` — user flows (currently in-memory user store)

## Project structure (high level)

- `app/` — application code (controllers, services, models, repositories, schemas)
- `tests/` — unit tests
- `requirements.txt`, `Dockerfile`, `pyproject.toml` — project and deploy files

## Deployment notes

- Set `DATABASE_URL` for production (Postgres recommended).
- Provide `SECRET_KEY` environment variable for Flask.
- Production run example using Gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 'app:create_app()'
```

Docker: there's a `Dockerfile` included; building and running the container is an option for deploying to a VM or App Service.

## CI/CD

- You can set up GitHub Actions to deploy to a VM via SSH or to a cloud App Service; include secrets for deploy credentials.

## Testing

Run unit tests with:

```bash
pytest
```

## License

MIT
