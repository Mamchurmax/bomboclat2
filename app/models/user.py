from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.extensions import db


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # relationships
    listings = db.relationship('Listing', back_populates='host', lazy=True)
    bookings = db.relationship('Booking', back_populates='guest', foreign_keys='Booking.guest_id', lazy=True)
    reviews = db.relationship('Review', back_populates='author', lazy=True)
    sent_messages = db.relationship('Message', back_populates='sender', foreign_keys='Message.sender_id', lazy=True)
    received_messages = db.relationship('Message', back_populates='receiver', foreign_keys='Message.receiver_id', lazy=True)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"