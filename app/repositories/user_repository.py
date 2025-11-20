class UserRepository:
    """A minimal in-memory user repository used to satisfy imports during app startup.

    This is intentionally simple: it stores user objects in a dict keyed by id and
    provides the methods used by `UserService`. It's a temporary, low-risk shim so
    the app can import modules and run; replace with a real DB-backed repository
    when wiring persistence.
    """
    def __init__(self):
        self._data = {}
        self._next_id = 1

    def save(self, user):
        # Assign an id if missing (simulate auto-increment)
        if getattr(user, 'id', None) is None:
            user.id = self._next_id
            self._next_id += 1
        self._data[user.id] = user
        return user

    def find_by_id(self, user_id):
        return self._data.get(user_id)

    def find_all(self):
        return list(self._data.values())

    def delete(self, user_id):
        return self._data.pop(user_id, None)
