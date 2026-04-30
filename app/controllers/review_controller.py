from flask import Blueprint, jsonify, request
from app.services.review_service import ReviewService

review_bp = Blueprint('review_bp', __name__, url_prefix='/reviews')
review_service = ReviewService()


def serialize_review(r):
    if r is None:
        return None
    return {
        "id": r.id,
        "listing_id": r.listing_id,
        "author_id": r.author_id,
        "rating": r.rating,
        "comment": r.comment,
        "created_at": r.created_at.isoformat() if r.created_at else None,
    }


@review_bp.route('/', methods=['GET'])
def get_reviews():
    """
    Get all reviews
    ---
    tags:
      - Reviews
    responses:
      200:
        description: A list of all reviews
    """
    reviews = review_service.get_all_reviews()
    return jsonify([serialize_review(r) for r in reviews]), 200


@review_bp.route('/', methods=['POST'])
def create_review():
    """
    Create a new review
    ---
    tags:
      - Reviews
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - listing_id
            - author_id
            - rating
          properties:
            listing_id:
              type: integer
            author_id:
              type: integer
            rating:
              type: integer
              minimum: 1
              maximum: 5
            comment:
              type: string
    responses:
      201:
        description: Review created
      400:
        description: Missing or invalid fields
    """
    data = request.json
    required = ('listing_id', 'author_id', 'rating')
    if not data or not all(k in data for k in required):
        return jsonify({"message": "Missing required fields", "required": list(required)}), 400

    try:
        data['rating'] = int(data['rating'])
        if not 1 <= data['rating'] <= 5:
            raise ValueError
    except (TypeError, ValueError):
        return jsonify({"message": "rating must be an integer between 1 and 5"}), 400

    review = review_service.create_review(data)
    return jsonify(serialize_review(review)), 201


@review_bp.route('/<int:review_id>', methods=['GET'])
def get_review(review_id):
    """
    Get a review by ID
    ---
    tags:
      - Reviews
    parameters:
      - name: review_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Review details
      404:
        description: Review not found
    """
    review = review_service.get_review_by_id(review_id)
    if review is None:
        return jsonify({"message": "Review not found"}), 404
    return jsonify(serialize_review(review)), 200


@review_bp.route('/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    """
    Update a review
    ---
    tags:
      - Reviews
    parameters:
      - name: review_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            rating:
              type: integer
              minimum: 1
              maximum: 5
            comment:
              type: string
    responses:
      200:
        description: Review updated
      404:
        description: Review not found
    """
    data = request.json
    review = review_service.update_review(review_id, data)
    if review is None:
        return jsonify({"message": "Review not found"}), 404
    return jsonify(serialize_review(review)), 200


@review_bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    """
    Delete a review
    ---
    tags:
      - Reviews
    parameters:
      - name: review_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Review deleted
      404:
        description: Review not found
    """
    success = review_service.delete_review(review_id)
    if not success:
        return jsonify({"message": "Review not found"}), 404
    return jsonify({"message": "Review deleted successfully"}), 200
