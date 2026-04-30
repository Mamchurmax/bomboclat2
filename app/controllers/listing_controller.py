from flask import Blueprint, jsonify, request
from app.services.listing_service import ListingService

listing_bp = Blueprint('listing_bp', __name__, url_prefix='/listings')
listing_service = ListingService()


def serialize_listing(listing):
    """Convert a Listing model instance to a JSON-serializable dict."""
    if listing is None:
        return None
    return {
        "id": getattr(listing, 'id', None),
        "title": getattr(listing, 'title', None),
        "description": getattr(listing, 'description', None),
        "price_per_night": getattr(listing, 'price_per_night', None),
        "location": getattr(listing, 'location', None),
        "host_id": getattr(listing, 'host_id', None),
        "amenities": [getattr(a, 'name', None) for a in getattr(listing, 'amenities', [])],
        "categories": [getattr(c, 'name', None) for c in getattr(listing, 'categories', [])],
    }


@listing_bp.route('/', methods=['GET'])
def get_listings():
    """
    Get all listings
    ---
    tags:
      - Listings
    responses:
      200:
        description: A list of all listings
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              title:
                type: string
              description:
                type: string
              price_per_night:
                type: number
              location:
                type: string
              host_id:
                type: integer
              amenities:
                type: array
                items:
                  type: string
              categories:
                type: array
                items:
                  type: string
    """
    listings = listing_service.get_all_listings()
    return jsonify([serialize_listing(l) for l in listings]), 200


@listing_bp.route('/', methods=['POST'])
def create_listing():
    """
    Create a new listing
    ---
    tags:
      - Listings
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - title
            - description
            - price_per_night
            - location
            - host_id
          properties:
            title:
              type: string
            description:
              type: string
            price_per_night:
              type: number
            location:
              type: string
            host_id:
              type: integer
    responses:
      201:
        description: Listing created successfully
      400:
        description: Missing required fields
    """
    data = request.json
    required = ('title', 'description', 'price_per_night', 'location', 'host_id')
    if not data or not all(k in data for k in required):
        return jsonify({
            "message": "Missing required fields",
            "required": list(required)
        }), 400

    try:
        data['price_per_night'] = float(data['price_per_night'])
    except (TypeError, ValueError):
        return jsonify({"message": "price_per_night must be a number"}), 400

    try:
        data['host_id'] = int(data['host_id'])
    except (TypeError, ValueError):
        return jsonify({"message": "host_id must be an integer"}), 400

    new_listing = listing_service.create_listing(data)
    return jsonify(serialize_listing(new_listing)), 201


@listing_bp.route('/<int:listing_id>', methods=['GET'])
def get_listing(listing_id):
    """
    Get a specific listing by ID
    ---
    tags:
      - Listings
    parameters:
      - name: listing_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Listing details
      404:
        description: Listing not found
    """
    listing = listing_service.get_listing_by_id(listing_id)
    if listing is None:
        return jsonify({"message": "Listing not found"}), 404
    return jsonify(serialize_listing(listing)), 200


@listing_bp.route('/<int:listing_id>', methods=['PUT'])
def update_listing(listing_id):
    """
    Update an existing listing
    ---
    tags:
      - Listings
    parameters:
      - name: listing_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            title:
              type: string
            description:
              type: string
            price_per_night:
              type: number
            location:
              type: string
    responses:
      200:
        description: Listing updated
      404:
        description: Listing not found
    """
    data = request.json
    updated_listing = listing_service.update_listing(listing_id, data)
    if updated_listing is None:
        return jsonify({"message": "Listing not found"}), 404
    return jsonify(serialize_listing(updated_listing)), 200


@listing_bp.route('/<int:listing_id>', methods=['DELETE'])
def delete_listing(listing_id):
    """
    Delete a listing
    ---
    tags:
      - Listings
    parameters:
      - name: listing_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Listing deleted successfully
      404:
        description: Listing not found
    """
    success = listing_service.delete_listing(listing_id)
    if not success:
        return jsonify({"message": "Listing not found"}), 404
    return jsonify({"message": "Listing deleted successfully"}), 200