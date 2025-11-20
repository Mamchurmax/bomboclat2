from app.extensions import db
from app.models.listing import Listing

class ListingRepository:
    def get_all_listings(self):
        return Listing.query.all()

    def get_listing_by_id(self, listing_id):
        return Listing.query.get(listing_id)

    def create_listing(self, listing_data):
        new_listing = Listing(**listing_data)
        db.session.add(new_listing)
        db.session.commit()
        return new_listing

    def update_listing(self, listing_id, listing_data):
        listing = self.get_listing_by_id(listing_id)
        if listing:
            for key, value in listing_data.items():
                setattr(listing, key, value)
            db.session.commit()
        return listing

    def delete_listing(self, listing_id):
        listing = self.get_listing_by_id(listing_id)
        if listing:
            db.session.delete(listing)
            db.session.commit()
        return listing

    # ----- Backwards-compatible short-named methods -----
    # Some services expect the shorter method names (get_all, get_by_id,
    # create, update, delete, get_amenities). Provide thin wrappers so both
    # naming styles work.
    def get_all(self):
        return self.get_all_listings()

    def get_by_id(self, listing_id):
        return self.get_listing_by_id(listing_id)

    def create(self, listing_data):
        return self.create_listing(listing_data)

    def update(self, listing_id, listing_data):
        return self.update_listing(listing_id, listing_data)

    def delete(self, listing_id):
        return self.delete_listing(listing_id)

    def get_amenities(self, listing_id):
        listing = self.get_listing_by_id(listing_id)
        if not listing:
            return None
        return getattr(listing, 'amenities', [])