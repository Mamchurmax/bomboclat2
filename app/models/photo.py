from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.extensions import db


class Photo(db.Model):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer, ForeignKey('listings.id'), nullable=False)
    url = Column(String(500), nullable=False)
    caption = Column(String(200), nullable=True)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    # relationships
    listing = db.relationship('Listing', back_populates='photos')

    def __repr__(self):
        return f'<Photo {self.id} listing={self.listing_id}>'
