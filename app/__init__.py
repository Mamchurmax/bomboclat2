from flask import Flask


def create_app():
    application = Flask(__name__)

    # Load configuration
    application.config.from_object('app.config.Config')

    # Initialize extensions
    from app.extensions import db, migrate
    db.init_app(application)
    migrate.init_app(application, db)

    # Import all models so Alembic sees them
    import app.models  # noqa: F401

    # Register blueprints
    from app.controllers import register_controllers
    register_controllers(application)

    # Swagger configuration
    from flasgger import Swagger
    swagger_template = {
        "info": {
            "title": "Airbnb Flask API",
            "description": "REST API for Airbnb-like application with listings, bookings, reviews, and more.",
            "version": "1.0.0",
        }
    }
    Swagger(application, template=swagger_template)

    @application.route('/hello')
    def hello():
        """
        A simple hello world endpoint
        ---
        tags:
          - Miscellaneous
        responses:
          200:
            description: A greeting message
        """
        return "Hello, this is a simple text response!"

    return application 
    