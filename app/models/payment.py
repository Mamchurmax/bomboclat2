from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from datetime import datetime
from app.extensions import db


class Payment(db.Model):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey('bookings.id'), nullable=False, unique=True)
    amount = Column(Float, nullable=False)
    method = Column(String(50), nullable=False)  # credit_card, paypal, bank_transfer
    status = Column(String(20), nullable=False, default='pending')  # pending, completed, refunded
    paid_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # relationships
    booking = db.relationship('Booking', back_populates='payment')

    def __repr__(self):
        return f'<Payment {self.id} amount={self.amount} status={self.status}>'
