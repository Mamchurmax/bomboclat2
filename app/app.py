from flask import Flask
from app.extensions import db, migrate
from app.controllers import register_controllers


def create_app():
    application = Flask(__name__)
    application.config.from_object('app.config.Config')

    db.init_app(application)
    migrate.init_app(application, db)

    # Import all models so Alembic sees them
    import app.models  # noqa: F401

    # Register blueprints
    register_controllers(application)

    # Swagger
    from flasgger import Swagger
    Swagger(application, template={
        "info": {
            "title": "Airbnb Flask API",
            "description": "REST API for Airbnb-like application",
            "version": "1.0.0",
        }
    })

    return application


if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=True)