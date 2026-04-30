from app.repositories.review_repository import ReviewRepository


class ReviewService:
    def __init__(self):
        self.repository = ReviewRepository()

    def get_all_reviews(self):
        return self.repository.get_all()

    def get_review_by_id(self, review_id):
        return self.repository.get_by_id(review_id)

    def create_review(self, data):
        return self.repository.create(data)

    def update_review(self, review_id, data):
        return self.repository.update(review_id, data)

    def delete_review(self, review_id):
        return self.repository.delete(review_id)

    def get_reviews_by_listing(self, listing_id):
        return self.repository.get_by_listing(listing_id)
