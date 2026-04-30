from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, CheckConstraint
from datetime import datetime
from app.extensions import db


class Review(db.Model):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer, ForeignKey('listings.id'), nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='ck_reviews_rating'),
    )

    # relationships
    listing = db.relationship('Listing', back_populates='reviews')
    author = db.relationship('User', back_populates='reviews')

    def __repr__(self):
        return f'<Review {self.id} rating={self.rating}>'
