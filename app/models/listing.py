from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from app.extensions import db

# association table for many-to-many relationship between listings and amenities
listing_amenities = db.Table(
    'listing_amenities',
    db.metadata,
    db.Column('listing_id', db.Integer, db.ForeignKey('listings.id')),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenities.id')),
)

# association table for many-to-many relationship between listings and categories
listing_categories = db.Table(
    'listing_categories',
    db.metadata,
    db.Column('listing_id', db.Integer, db.ForeignKey('listings.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id')),
)


class Listing(db.Model):
    __tablename__ = 'listings'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    price_per_night = Column(Float, nullable=False)
    location = Column(String(100), nullable=False)
    host_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    # relationships
    host = db.relationship('User', back_populates='listings')
    amenities = db.relationship('Amenity', secondary=listing_amenities, back_populates='listings')
    categories = db.relationship('Category', secondary=listing_categories, back_populates='listings')
    bookings = db.relationship('Booking', back_populates='listing', lazy=True)
    reviews = db.relationship('Review', back_populates='listing', lazy=True)
    photos = db.relationship('Photo', back_populates='listing', lazy=True)

    def __init__(self, title, description, price_per_night, location, host_id):
        self.title = title
        self.description = description
        self.price_per_night = price_per_night
        self.location = location
        self.host_id = host_id

    def __repr__(self):
        return f'<Listing {self.title}>'