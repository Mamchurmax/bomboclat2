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
        # keep the API field name as `price` (map from model's price_per_night)
        "price": getattr(listing, 'price_per_night', None),
        "location": getattr(listing, 'location', None),
        "host_id": getattr(listing, 'host_id', None),
        "amenities": [getattr(a, 'name', None) for a in getattr(listing, 'amenities', [])]
    }

# 1. READ (All) - Retrieve all listings
@listing_bp.route('/', methods=['GET'])
def get_listings():
    listings = listing_service.get_all_listings()
    # serialize model instances to plain dicts
    return jsonify([serialize_listing(l) for l in listings]), 200

# 2. CREATE - Insert a new listing
@listing_bp.route('/', methods=['POST'])
def create_listing():
    data = request.json
    # Require the full set of fields expected by the Listing model/constructor
    required = ('title', 'description', 'price_per_night', 'location', 'host_id')
    if not data or not all(k in data for k in required):
        return jsonify({
            "message": "Missing required fields",
            "required": list(required)
        }), 400

    # Validate simple types: price should be a number, host_id an int
    try:
        data['price_per_night'] = float(data['price_per_night'])
    except (TypeError, ValueError):
        return jsonify({"message": "price_per_night must be a number"}), 400

    try:
        data['host_id'] = int(data['host_id'])
    except (TypeError, ValueError):
        return jsonify({"message": "host_id must be an integer"}), 400

    # Delegate creation to the service (may still raise DB errors if migrations
    # haven't been applied; this validation avoids the common TypeError seen
    # when required fields are missing).
    new_listing = listing_service.create_listing(data)
    return jsonify(serialize_listing(new_listing)), 201

# 3. READ (Single) - Retrieve a specific listing by ID
@listing_bp.route('/<int:listing_id>', methods=['GET'])
def get_listing(listing_id):
    listing = listing_service.get_listing_by_id(listing_id)
    if listing is None:
        return jsonify({"message": "Listing not found"}), 404
    return jsonify(serialize_listing(listing)), 200

# 4. UPDATE - Update an existing listing
@listing_bp.route('/<int:listing_id>', methods=['PUT'])
def update_listing(listing_id):
    data = request.json
    updated_listing = listing_service.update_listing(listing_id, data)
    if updated_listing is None:
        return jsonify({"message": "Listing not found"}), 404
    return jsonify(serialize_listing(updated_listing)), 200

# 5. DELETE - Delete a listing
@listing_bp.route('/<int:listing_id>', methods=['DELETE'])
def delete_listing(listing_id):
    success = listing_service.delete_listing(listing_id)
    if not success:
        return jsonify({"message": "Listing not found"}), 404
    return jsonify({"message": "Listing deleted successfully"}), 204