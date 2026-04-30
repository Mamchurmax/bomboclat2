from flask import Blueprint, jsonify, request
from app.services.message_service import MessageService

message_bp = Blueprint('message_bp', __name__, url_prefix='/messages')
message_service = MessageService()


def serialize_message(m):
    if m is None:
        return None
    return {
        "id": m.id, "sender_id": m.sender_id, "receiver_id": m.receiver_id,
        "body": m.body, "is_read": m.is_read,
        "created_at": m.created_at.isoformat() if m.created_at else None,
    }


@message_bp.route('/', methods=['GET'])
def get_messages():
    """Get all messages
    ---
    tags: [Messages]
    responses:
      200: {description: List of messages}
    """
    return jsonify([serialize_message(m) for m in message_service.get_all_messages()]), 200


@message_bp.route('/', methods=['POST'])
def create_message():
    """Create a message
    ---
    tags: [Messages]
    parameters:
      - {in: body, name: body, required: true, schema: {type: object, required: [sender_id, receiver_id, body], properties: {sender_id: {type: integer}, receiver_id: {type: integer}, body: {type: string}}}}
    responses:
      201: {description: Created}
      400: {description: Missing fields}
    """
    data = request.json
    required = ('sender_id', 'receiver_id', 'body')
    if not data or not all(k in data for k in required):
        return jsonify({"message": "Missing required fields", "required": list(required)}), 400
    return jsonify(serialize_message(message_service.create_message(data))), 201


@message_bp.route('/<int:mid>', methods=['GET'])
def get_message(mid):
    """Get message by ID
    ---
    tags: [Messages]
    parameters:
      - {name: mid, in: path, type: integer, required: true}
    responses:
      200: {description: Message details}
      404: {description: Not found}
    """
    m = message_service.get_message_by_id(mid)
    if m is None:
        return jsonify({"message": "Message not found"}), 404
    return jsonify(serialize_message(m)), 200


@message_bp.route('/<int:mid>', methods=['PUT'])
def update_message(mid):
    """Update a message
    ---
    tags: [Messages]
    parameters:
      - {name: mid, in: path, type: integer, required: true}
      - {in: body, name: body, schema: {type: object, properties: {is_read: {type: boolean}}}}
    responses:
      200: {description: Updated}
      404: {description: Not found}
    """
    m = message_service.update_message(mid, request.json)
    if m is None:
        return jsonify({"message": "Message not found"}), 404
    return jsonify(serialize_message(m)), 200


@message_bp.route('/<int:mid>', methods=['DELETE'])
def delete_message(mid):
    """Delete a message
    ---
    tags: [Messages]
    parameters:
      - {name: mid, in: path, type: integer, required: true}
    responses:
      200: {description: Deleted}
      404: {description: Not found}
    """
    if not message_service.delete_message(mid):
        return jsonify({"message": "Message not found"}), 404
    return jsonify({"message": "Message deleted"}), 200
