from app.extensions import db
from app.models.amenity import Amenity
from sqlalchemy.exc import IntegrityError

class AmenityRepository:
    def get_all_amenities(self):
        return Amenity.query.all()

    def get_amenity_by_id(self, amenity_id):
        return Amenity.query.get(amenity_id)

    def get_by_name(self, name):
        return Amenity.query.filter_by(name=name).first()

    def create_amenity(self, name):
        # Fast path: if amenity already exists, return it
        existing = self.get_by_name(name)
        if existing:
            return existing

        # Otherwise attempt to create; handle race/unique constraint gracefully
        amenity = Amenity(name=name)
        db.session.add(amenity)
        try:
            db.session.commit()
            return amenity
        except IntegrityError:
            # Another transaction inserted the same name concurrently.
            db.session.rollback()
            return self.get_by_name(name)

    def update_amenity(self, amenity_id, name):
        amenity = self.get_amenity_by_id(amenity_id)
        if amenity:
            amenity.name = name
            db.session.commit()
        return amenity

    def delete_amenity(self, amenity_id):
        amenity = self.get_amenity_by_id(amenity_id)
        if amenity:
            db.session.delete(amenity)
            db.session.commit()
        return amenity