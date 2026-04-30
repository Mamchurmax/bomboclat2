from app.repositories.photo_repository import PhotoRepository


class PhotoService:
    def __init__(self):
        self.repository = PhotoRepository()

    def get_all_photos(self):
        return self.repository.get_all()

    def get_photo_by_id(self, photo_id):
        return self.repository.get_by_id(photo_id)

    def create_photo(self, data):
        return self.repository.create(data)

    def update_photo(self, photo_id, data):
        return self.repository.update(photo_id, data)

    def delete_photo(self, photo_id):
        return self.repository.delete(photo_id)

    def get_photos_by_listing(self, listing_id):
        return self.repository.get_by_listing(listing_id)
