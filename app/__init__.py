from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('app.config.Config')

    # Initialize extensions
    from app.extensions import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.controllers.listing_controller import listing_bp
    from app.controllers.amenity_controller import amenity_bp
    from app.controllers.user_controller import user_bp

    app.register_blueprint(listing_bp)
    app.register_blueprint(amenity_bp)
    app.register_blueprint(user_bp)

    return app