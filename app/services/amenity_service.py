from app.repositories.amenity_repository import AmenityRepository
from sqlalchemy.exc import IntegrityError
from app.extensions import db


class AmenityService:
    def __init__(self):
        self.repository = AmenityRepository()

    def get_all_amenities(self):
        return self.repository.get_all_amenities()

    def create_amenity(self, data):
        # controller passes JSON body with 'name'
        name = data.get('name') if isinstance(data, dict) else data
        # avoid unique constraint errors: return existing amenity if name exists
        existing = self.repository.get_by_name(name)
        if existing:
            return existing

        try:
            return self.repository.create_amenity(name)
        except IntegrityError:
            # Another request may have created it concurrently. Rollback and
            # return the existing record.
            db.session.rollback()
            existing = self.repository.get_by_name(name)
            if existing:
                return existing
            raise

    def get_amenities_for_listing(self, listing_id):
        # If needed, delegate to listing repository or implement repo method
        return None