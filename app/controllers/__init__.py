from .listing_controller import listing_bp as listing_bp
from .amenity_controller import amenity_bp as amenity_bp
from .user_controller import user_bp as user_bp

def register_controllers(app):
    app.register_blueprint(listing_bp)
    app.register_blueprint(amenity_bp)
    app.register_blueprint(user_bp)