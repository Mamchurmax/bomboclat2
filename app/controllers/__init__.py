from .listing_controller import listing_bp
from .amenity_controller import amenity_bp
from .user_controller import user_bp
from .booking_controller import booking_bp
from .review_controller import review_bp
from .category_controller import category_bp
from .photo_controller import photo_bp
from .payment_controller import payment_bp
from .message_controller import message_bp


def register_controllers(app):
    app.register_blueprint(listing_bp)
    app.register_blueprint(amenity_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(photo_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(message_bp)