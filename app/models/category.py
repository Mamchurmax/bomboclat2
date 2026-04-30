from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.extensions import db


class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(255), nullable=True)

    listings = relationship('Listing', secondary='listing_categories', back_populates='categories')

    def __repr__(self):
        return f'<Category {self.name}>'
