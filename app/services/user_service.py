from app.models.user import User
from app.repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash
from types import SimpleNamespace
from datetime import datetime
import uuid


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, user_data):
        # Legacy helper: create a user-like object and persist via repo.
        user = SimpleNamespace(**user_data)
        return self.user_repository.save(user)

    def register_user(self, user_data):
        # Expecting {'username': str, 'password': str, 'email': optional}
        username = user_data.get('username')
        password = user_data.get('password')
        email = user_data.get('email', '')
        if not username or not password:
            return None

        password_hash = generate_password_hash(password)
        user_obj = SimpleNamespace(
            username=username,
            email=email,
            password_hash=password_hash,
            created_at=datetime.utcnow().isoformat()
        )

        saved = self.user_repository.save(user_obj)
        # Return a serializable dict (do not expose password_hash)
        return {
            'id': getattr(saved, 'id', None),
            'username': getattr(saved, 'username', None),
            'email': getattr(saved, 'email', None),
            'created_at': getattr(saved, 'created_at', None)
        }

    def authenticate_user(self, credentials):
        username = credentials.get('username')
        password = credentials.get('password')
        if not username or not password:
            return None

        # Search users in repository
        for u in self.user_repository.find_all():
            if getattr(u, 'username', None) == username:
                stored_hash = getattr(u, 'password_hash', None)
                if stored_hash and check_password_hash(stored_hash, password):
                    # return a simple token (UUID) — replace with JWT if needed
                    return str(uuid.uuid4())
        return None

    def get_user_by_id(self, user_id):
        u = self.user_repository.find_by_id(user_id)
        if not u:
            return None
        return {
            'id': getattr(u, 'id', None),
            'username': getattr(u, 'username', None),
            'email': getattr(u, 'email', None),
            'created_at': getattr(u, 'created_at', None)
        }

    def get_all_users(self):
        return [
            {
                'id': getattr(u, 'id', None),
                'username': getattr(u, 'username', None),
                'email': getattr(u, 'email', None),
                'created_at': getattr(u, 'created_at', None)
            }
            for u in self.user_repository.find_all()
        ]

    def update_user(self, user_id, user_data):
        user = self.user_repository.find_by_id(user_id)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            saved = self.user_repository.save(user)
            return {
                'id': getattr(saved, 'id', None),
                'username': getattr(saved, 'username', None),
                'email': getattr(saved, 'email', None),
                'created_at': getattr(saved, 'created_at', None)
            }
        return None

    def delete_user(self, user_id):
        return self.user_repository.delete(user_id)