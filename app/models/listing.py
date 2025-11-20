from sqlalchemy import Column, Integer, String, Text, Float
from app.extensions import db

# association table for many-to-many relationship between listings and amenities
listing_amenities = db.Table(
    'listing_amenities',
    db.metadata,
    db.Column('listing_id', db.Integer, db.ForeignKey('listings.id')),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenities.id')),
)


class Listing(db.Model):
    __tablename__ = 'listings'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    price_per_night = Column(Float, nullable=False)
    location = Column(String(100), nullable=False)
    host_id = Column(Integer, nullable=False)  # Assuming a foreign key to a User model

    # relationship to amenities (many-to-many)
    amenities = db.relationship('Amenity', secondary=listing_amenities, back_populates='listings')

    def __init__(self, title, description, price_per_night, location, host_id):
        self.title = title
        self.description = description
        self.price_per_night = price_per_night
        self.location = location
        self.host_id = host_id

    def __repr__(self):
        return f'<Listing {self.title}>'