from flask import Blueprint, jsonify, request
from app.services.user_service import UserService

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')
user_service = UserService()

# 1. REGISTER - User registration
@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"message": "Username and password are required"}), 400
    
    new_user = user_service.register_user(data)
    return jsonify(new_user), 201

# 2. LOGIN - User authentication
@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"message": "Username and password are required"}), 400
    
    token = user_service.authenticate_user(data)
    if not token:
        return jsonify({"message": "Invalid credentials"}), 401
    
    return jsonify({"token": token}), 200

# 3. GET USER - Retrieve user information
@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    
    return jsonify(user), 200

# 4. UPDATE USER - Update user information
@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    updated_user = user_service.update_user(user_id, data)
    if updated_user is None:
        return jsonify({"message": "User not found"}), 404
    
    return jsonify(updated_user), 200

# 5. DELETE USER - Remove a user
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = user_service.delete_user(user_id)
    if not success:
        return jsonify({"message": "User not found"}), 404
    
    return jsonify({"message": "User deleted successfully"}), 204