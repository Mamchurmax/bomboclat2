from flask import Blueprint, jsonify, request
from app.services.amenity_service import AmenityService
from sqlalchemy.exc import IntegrityError
from app.extensions import db
from app.services.listing_service import ListingService
from app.controllers.listing_controller import listing_bp

amenity_bp = Blueprint('amenity_bp', __name__, url_prefix='/amenities')
amenity_service = AmenityService()
listing_service = ListingService()

@amenity_bp.route('/', methods=['GET'])
def get_amenities():
    amenities = amenity_service.get_all_amenities()
    # serialize Amenity model instances to dicts
    result = [{"id": getattr(a, 'id', None), "name": getattr(a, 'name', None)} for a in amenities]
    return jsonify(result), 200

@amenity_bp.route('/', methods=['POST'])
def create_amenity():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"message": "Amenity name required"}), 400
    # Check existing amenities first to avoid unique constraint errors
    try:
        existing = [a for a in amenity_service.get_all_amenities() if getattr(a, 'name', None) == data['name']]
        if existing:
            a = existing[0]
            return jsonify({"id": getattr(a, 'id', None), "name": getattr(a, 'name', None), "message": "already exists"}), 200

        new_amenity = amenity_service.create_amenity(data)
        return jsonify({"id": getattr(new_amenity, 'id', None), "name": getattr(new_amenity, 'name', None)}), 201
    except IntegrityError:
        # concurrent insert happened; rollback and return existing
        db.session.rollback()
        existing = [a for a in amenity_service.get_all_amenities() if getattr(a, 'name', None) == data['name']]
        if existing:
            a = existing[0]
            return jsonify({"id": getattr(a, 'id', None), "name": getattr(a, 'name', None), "message": "already exists"}), 200
        raise

@listing_bp.route('/<int:listing_id>/amenities', methods=['GET'])
def get_amenities_for_listing(listing_id):
    amenities = listing_service.get_amenities_for_listing(listing_id)
    if amenities is None:
        return jsonify({"message": "Listing not found"}), 404
        
    # return amenity names for the listing
    names = [getattr(a, 'name', None) for a in amenities]
    return jsonify({"listing_id": listing_id, "amenities": names}), 200