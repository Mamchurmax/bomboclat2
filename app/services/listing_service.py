from app.repositories.listing_repository import ListingRepository

class ListingService:
    def __init__(self):
        self.listing_repository = ListingRepository()

    def get_all_listings(self):
        return self.listing_repository.get_all()

    def get_listing_by_id(self, listing_id):
        return self.listing_repository.get_by_id(listing_id)

    def create_listing(self, data):
        return self.listing_repository.create(data)

    def update_listing(self, listing_id, data):
        return self.listing_repository.update(listing_id, data)

    def delete_listing(self, listing_id):
        return self.listing_repository.delete(listing_id)

    def get_amenities_for_listing(self, listing_id):
        return self.listing_repository.get_amenities(listing_id)