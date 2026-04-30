from flask import Blueprint, jsonify, request
from app.services.photo_service import PhotoService

photo_bp = Blueprint('photo_bp', __name__, url_prefix='/photos')
photo_service = PhotoService()


def serialize_photo(p):
    if p is None:
        return None
    return {
        "id": p.id, "listing_id": p.listing_id, "url": p.url,
        "caption": p.caption,
        "uploaded_at": p.uploaded_at.isoformat() if p.uploaded_at else None,
    }


@photo_bp.route('/', methods=['GET'])
def get_photos():
    """Get all photos
    ---
    tags: [Photos]
    responses:
      200: {description: List of photos}
    """
    return jsonify([serialize_photo(p) for p in photo_service.get_all_photos()]), 200


@photo_bp.route('/', methods=['POST'])
def create_photo():
    """Create a photo
    ---
    tags: [Photos]
    parameters:
      - {in: body, name: body, required: true, schema: {type: object, required: [listing_id, url], properties: {listing_id: {type: integer}, url: {type: string}, caption: {type: string}}}}
    responses:
      201: {description: Created}
      400: {description: Missing fields}
    """
    data = request.json
    if not data or 'listing_id' not in data or 'url' not in data:
        return jsonify({"message": "listing_id and url required"}), 400
    return jsonify(serialize_photo(photo_service.create_photo(data))), 201


@photo_bp.route('/<int:pid>', methods=['GET'])
def get_photo(pid):
    """Get photo by ID
    ---
    tags: [Photos]
    parameters:
      - {name: pid, in: path, type: integer, required: true}
    responses:
      200: {description: Photo details}
      404: {description: Not found}
    """
    p = photo_service.get_photo_by_id(pid)
    if p is None:
        return jsonify({"message": "Photo not found"}), 404
    return jsonify(serialize_photo(p)), 200


@photo_bp.route('/<int:pid>', methods=['PUT'])
def update_photo(pid):
    """Update a photo
    ---
    tags: [Photos]
    parameters:
      - {name: pid, in: path, type: integer, required: true}
      - {in: body, name: body, schema: {type: object, properties: {url: {type: string}, caption: {type: string}}}}
    responses:
      200: {description: Updated}
      404: {description: Not found}
    """
    p = photo_service.update_photo(pid, request.json)
    if p is None:
        return jsonify({"message": "Photo not found"}), 404
    return jsonify(serialize_photo(p)), 200


@photo_bp.route('/<int:pid>', methods=['DELETE'])
def delete_photo(pid):
    """Delete a photo
    ---
    tags: [Photos]
    parameters:
      - {name: pid, in: path, type: integer, required: true}
    responses:
      200: {description: Deleted}
      404: {description: Not found}
    """
    if not photo_service.delete_photo(pid):
        return jsonify({"message": "Photo not found"}), 404
    return jsonify({"message": "Photo deleted"}), 200
