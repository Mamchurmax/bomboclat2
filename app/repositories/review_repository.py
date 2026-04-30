from app.extensions import db
from app.models.review import Review


class ReviewRepository:
    def get_all(self):
        return Review.query.all()

    def get_by_id(self, review_id):
        return db.session.get(Review, review_id)

    def create(self, data):
        review = Review(**data)
        db.session.add(review)
        db.session.commit()
        return review

    def update(self, review_id, data):
        review = self.get_by_id(review_id)
        if review:
            for key, value in data.items():
                setattr(review, key, value)
            db.session.commit()
        return review

    def delete(self, review_id):
        review = self.get_by_id(review_id)
        if review:
            db.session.delete(review)
            db.session.commit()
            return True
        return False

    def get_by_listing(self, listing_id):
        return Review.query.filter_by(listing_id=listing_id).all()
