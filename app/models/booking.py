from sqlalchemy import Column, Integer, Float, DateTime, String, ForeignKey
from datetime import datetime
from app.extensions import db


class Booking(db.Model):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer, ForeignKey('listings.id'), nullable=False)
    guest_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    check_in = Column(DateTime, nullable=False)
    check_out = Column(DateTime, nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String(20), nullable=False, default='pending')  # pending, confirmed, cancelled
    created_at = Column(DateTime, default=datetime.utcnow)

    # relationships
    listing = db.relationship('Listing', back_populates='bookings')
    guest = db.relationship('User', back_populates='bookings', foreign_keys=[guest_id])
    payment = db.relationship('Payment', back_populates='booking', uselist=False)

    def __repr__(self):
        return f'<Booking {self.id} listing={self.listing_id} guest={self.guest_id}>'
