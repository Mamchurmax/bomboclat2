from app.extensions import db
from app.models.user import User


class UserRepository:
    """Database-backed user repository using SQLAlchemy."""

    def save(self, user_obj):
        """Create or update a user. Accepts a SimpleNamespace or User instance."""
        if isinstance(user_obj, User):
            db.session.add(user_obj)
            db.session.commit()
            return user_obj

        # Build a User model from a namespace / dict-like object
        user = User(
            username=getattr(user_obj, 'username', None),
            email=getattr(user_obj, 'email', ''),
            password_hash=getattr(user_obj, 'password_hash', ''),
        )
        db.session.add(user)
        db.session.commit()
        return user

    def find_by_id(self, user_id):
        return db.session.get(User, user_id)

    def find_all(self):
        return User.query.all()

    def find_by_username(self, username):
        return User.query.filter_by(username=username).first()

    def delete(self, user_id):
        user = self.find_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return user
        return None
