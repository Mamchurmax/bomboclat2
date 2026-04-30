from flask import Blueprint, jsonify, request
from app.services.user_service import UserService

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')
user_service = UserService()


@user_bp.route('/register', methods=['POST'])
def register_user():
    """
    Register a new user
    ---
    tags:
      - Users
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
            password:
              type: string
            email:
              type: string
    responses:
      201:
        description: User registered
      400:
        description: Missing fields
    """
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"message": "Username and password are required"}), 400

    new_user = user_service.register_user(data)
    return jsonify(new_user), 201


@user_bp.route('/login', methods=['POST'])
def login_user():
    """
    Authenticate user
    ---
    tags:
      - Users
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: Login successful, returns token
      401:
        description: Invalid credentials
    """
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"message": "Username and password are required"}), 400

    token = user_service.authenticate_user(data)
    if not token:
        return jsonify({"message": "Invalid credentials"}), 401

    return jsonify({"token": token}), 200


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get user by ID
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: User details
      404:
        description: User not found
    """
    user = user_service.get_user_by_id(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404

    return jsonify(user), 200


@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update user information
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            username:
              type: string
            email:
              type: string
    responses:
      200:
        description: User updated
      404:
        description: User not found
    """
    data = request.json
    updated_user = user_service.update_user(user_id, data)
    if updated_user is None:
        return jsonify({"message": "User not found"}), 404

    return jsonify(updated_user), 200


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: User deleted
      404:
        description: User not found
    """
    success = user_service.delete_user(user_id)
    if not success:
        return jsonify({"message": "User not found"}), 404

    return jsonify({"message": "User deleted successfully"}), 200