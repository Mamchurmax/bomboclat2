from flask import Blueprint, jsonify, request
from app.services.category_service import CategoryService

category_bp = Blueprint('category_bp', __name__, url_prefix='/categories')
category_service = CategoryService()


def serialize_category(c):
    if c is None:
        return None
    return {"id": c.id, "name": c.name, "description": getattr(c, 'description', None)}


@category_bp.route('/', methods=['GET'])
def get_categories():
    """Get all categories
    ---
    tags: [Categories]
    responses:
      200: {description: List of categories}
    """
    return jsonify([serialize_category(c) for c in category_service.get_all_categories()]), 200


@category_bp.route('/', methods=['POST'])
def create_category():
    """Create a category
    ---
    tags: [Categories]
    parameters:
      - {in: body, name: body, required: true, schema: {type: object, required: [name], properties: {name: {type: string}, description: {type: string}}}}
    responses:
      201: {description: Created}
      400: {description: Name required}
    """
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"message": "Category name required"}), 400
    return jsonify(serialize_category(category_service.create_category(data))), 201


@category_bp.route('/<int:cid>', methods=['GET'])
def get_category(cid):
    """Get category by ID
    ---
    tags: [Categories]
    parameters:
      - {name: cid, in: path, type: integer, required: true}
    responses:
      200: {description: Category details}
      404: {description: Not found}
    """
    c = category_service.get_category_by_id(cid)
    if c is None:
        return jsonify({"message": "Category not found"}), 404
    return jsonify(serialize_category(c)), 200


@category_bp.route('/<int:cid>', methods=['PUT'])
def update_category(cid):
    """Update a category
    ---
    tags: [Categories]
    parameters:
      - {name: cid, in: path, type: integer, required: true}
      - {in: body, name: body, schema: {type: object, properties: {name: {type: string}, description: {type: string}}}}
    responses:
      200: {description: Updated}
      404: {description: Not found}
    """
    c = category_service.update_category(cid, request.json)
    if c is None:
        return jsonify({"message": "Category not found"}), 404
    return jsonify(serialize_category(c)), 200


@category_bp.route('/<int:cid>', methods=['DELETE'])
def delete_category(cid):
    """Delete a category
    ---
    tags: [Categories]
    parameters:
      - {name: cid, in: path, type: integer, required: true}
    responses:
      200: {description: Deleted}
      404: {description: Not found}
    """
    if not category_service.delete_category(cid):
        return jsonify({"message": "Category not found"}), 404
    return jsonify({"message": "Category deleted"}), 200
