from app.extensions import db
from app.models.photo import Photo


class PhotoRepository:
    def get_all(self):
        return Photo.query.all()

    def get_by_id(self, photo_id):
        return db.session.get(Photo, photo_id)

    def create(self, data):
        photo = Photo(**data)
        db.session.add(photo)
        db.session.commit()
        return photo

    def update(self, photo_id, data):
        photo = self.get_by_id(photo_id)
        if photo:
            for key, value in data.items():
                setattr(photo, key, value)
            db.session.commit()
        return photo

    def delete(self, photo_id):
        photo = self.get_by_id(photo_id)
        if photo:
            db.session.delete(photo)
            db.session.commit()
            return True
        return False

    def get_by_listing(self, listing_id):
        return Photo.query.filter_by(listing_id=listing_id).all()
