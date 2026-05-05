from flask import Blueprint, jsonify, request
from app.services.amenity_service import AmenityService
from sqlalchemy.exc import IntegrityError
from app.extensions import db

amenity_bp = Blueprint('amenity_bp', __name__, url_prefix='/amenities')
amenity_service = AmenityService()


@amenity_bp.route('/', methods=['GET'])
def get_amenities():
    """
    Get all amenities
    ---
    tags:
      - Amenities
    responses:
      200:
        description: A list of all amenities
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
    """
    amenities = amenity_service.get_all_amenities()
    result = [{"id": getattr(a, 'id', None), "name": getattr(a, 'name', None)} for a in amenities]
    return jsonify(result), 200


@amenity_bp.route('/', methods=['POST'])
def create_amenity():
    """
    Create a new amenity
    ---
    tags:
      - Amenities
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
          properties:
            name:
              type: string
    responses:
      201:
        description: Amenity created
      200:
        description: Amenity already exists
      400:
        description: Name required
    """
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"message": "Amenity name required"}), 400
    try:
        existing = [a for a in amenity_service.get_all_amenities() if getattr(a, 'name', None) == data['name']]
        if existing:
            a = existing[0]
            return jsonify({"id": getattr(a, 'id', None), "name": getattr(a, 'name', None), "message": "already exists"}), 200

        new_amenity = amenity_service.create_amenity(data)
        return jsonify({"id": getattr(new_amenity, 'id', None), "name": getattr(new_amenity, 'name', None)}), 201
    except IntegrityError:
        db.session.rollback()
        existing = [a for a in amenity_service.get_all_amenities() if getattr(a, 'name', None) == data['name']]
        if existing:
            a = existing[0]
            return jsonify({"id": getattr(a, 'id', None), "name": getattr(a, 'name', None), "message": "already exists"}), 200
        raise