from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.extensions import db


class Amenity(db.Model):
    __tablename__ = 'amenities'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    listings = relationship('Listing', secondary='listing_amenities', back_populates='amenities')

    def __repr__(self):
        return f'<Amenity {self.name}>'